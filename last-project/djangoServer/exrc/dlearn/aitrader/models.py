import os
from abc import ABCMeta, abstractmethod
from enum import Enum

import numpy as np
from keras import Sequential, Input, Model
from keras.callbacks import EarlyStopping
from keras.layers import Dense, LSTM, concatenate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from api.path import dir_path


class ModelType(Enum):
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4


class H5FileNames(Enum):
    dnn_model = "samsung_stock_dnn_model.h5"
    dnn_ensemble = "samsung_stock_dnn_ensemble.h5"
    lstm_model = "samsung_stock_lstm_model.h5"
    lstm_ensemble = "samsung_stock_lstm_ensemble.h5"


class AiTradeBase(metaclass=ABCMeta):
    @abstractmethod
    def split_xy5(self, **kwargs): pass

    @abstractmethod
    def create(self): pass


class AiTraderModel(AiTradeBase):

    def __init__(self):
        global kospi200, samsung
        kospi200 = np.load(os.path.join(dir_path("aitrader"), "save", "processed_kospi200.npy"), allow_pickle=True)
        samsung = np.load(os.path.join(dir_path("aitrader"), "save", "processed_samsung.npy"), allow_pickle=True)

    def split_xy5(self, dataset, time_steps, y_column):
        x, y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column

            if y_end_number > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :]
            tmp_y = dataset[x_end_number:y_end_number, 3]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def save(self, *params):
        pass

    @abstractmethod
    def test(self, *params):
        pass

    @abstractmethod
    def training(self, *params):
        pass

    @abstractmethod
    def modeling(self):
        pass

    @abstractmethod
    def scaled(self):
        pass


class DnnModel(AiTraderModel):

    def create(self):
        x_test_scaled, x_train_scaled, y_test, y_train = self.scaled()
        model = self.modeling()
        self.training(model, x_train_scaled, y_train)
        self.test(model, x_test_scaled, y_test)
        self.save(model)

    def save(self, model):
        file_name = os.path.join(dir_path("aitrader"), "save", H5FileNames.dnn_model.value)
        model.save(file_name)

    def test(self, model, x_test_scaled, y_test):
        x_test_scaled = x_test_scaled.astype(np.float32)
        y_test = y_test.astype(np.float32)
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print(f"loss : {loss}\n"
              f"mse : {mse}")
        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print(f"종가 : {y_test[i]} / 예측가 : {y_pred[i]}")

    def training(self, model, x_train_scaled, y_train):
        early_stopping = EarlyStopping(patience=20)
        x_train_scaled = x_train_scaled.astype(np.float32)
        y_train = y_train.astype(np.float32)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

    def modeling(self):
        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        return model

    def scaled(self):
        x, y = self.split_xy5(samsung, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        return x_test_scaled, x_train_scaled, y_test, y_train


class DnnEnsemble(AiTraderModel):

    def create(self):
        x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train = self.scaled()
        model = self.modeling()
        self.training(model, x1_train_scaled, x2_train_scaled, y1_train)
        self.test(model, x1_test_scaled, x2_test_scaled, y1_test)
        self.save(model)

    def save(self, model):
        file_name = os.path.join(dir_path("aitrader"), "save", H5FileNames.dnn_ensemble.value)
        model.save(file_name)

    def test(self, model, x1_test_scaled, x2_test_scaled, y1_test):
        x1_test_scaled = x1_test_scaled.astype(np.float32)
        x2_test_scaled = x2_test_scaled.astype(np.float32)
        y1_test = y1_test.astype(np.float32)
        loss, mse = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)
        print(f"loss : {loss}\n"
              f"mse : {mse}")
        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])
        for i in range(5):
            print(f"종가 : {y1_test[i]} / 예측가 : {y1_pred[i]}")

    def training(self, model, x1_train_scaled, x2_train_scaled, y1_train):
        early_stopping = EarlyStopping(patience=20)
        x1_train_scaled = x1_train_scaled.astype(np.float32)
        x2_train_scaled = x2_train_scaled.astype(np.float32)
        y1_train = y1_train.astype(np.float32)
        model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2,
                  verbose=1, batch_size=1, epochs=100, callbacks=[early_stopping])

    def modeling(self):
        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)
        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)
        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        return model

    def scaled(self):
        x1, y1 = self.split_xy5(samsung, 5, 1)
        x2, y2 = self.split_xy5(kospi200, 5, 1)
        x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=1, test_size=0.3)
        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=2, test_size=0.3)
        x1_train = np.reshape(x1_train, (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
        x1_test = np.reshape(x1_test, (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))
        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))
        scaler1 = StandardScaler()
        scaler1.fit(x1_train)
        x1_train_scaled = scaler1.transform(x1_train)
        x1_test_scaled = scaler1.transform(x1_test)
        scaler2 = StandardScaler()
        scaler2.fit(x2_train)
        x2_train_scaled = scaler2.transform(x2_train)
        x2_test_scaled = scaler2.transform(x2_test)
        return x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train


class LstmModel(AiTraderModel):

    def create(self):
        x_test_scaled, x_train_scaled, y_test, y_train = self.scaled()
        model = self.modeling()
        self.training(model, x_train_scaled, y_train)
        self.test(model, x_test_scaled, y_test)
        self.save(model)

    def save(self, model):
        file_name = os.path.join(dir_path("aitrader"), "save", H5FileNames.lstm_model.value)
        model.save(file_name)

    def test(self, model, x_test_scaled, y_test):
        x_test_scaled = x_test_scaled.astype(np.float32)
        y_test = y_test.astype(np.float32)
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print(f"loss : {loss}\n"
              f"mse : {mse}")
        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print(f"종가 : {y_test[i]} / 예측가 : {y_pred[i]}")

    def training(self, model, x_train_scaled, y_train):
        early_stopping = EarlyStopping(patience=20)
        x_train_scaled = x_train_scaled.astype(np.float32)
        y_train = y_train.astype(np.float32)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

    def modeling(self):
        model = Sequential()
        model.add(LSTM(64, input_shape=(5, 5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics='mse')
        return model

    def scaled(self):
        x, y = self.split_xy5(samsung, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        x_train_scaled = np.reshape(x_train_scaled,
                                    (x_train_scaled.shape[0], 5, 5))
        x_test_scaled = np.reshape(x_test_scaled,
                                   (x_test_scaled.shape[0], 5, 5))
        return x_test_scaled, x_train_scaled, y_test, y_train


class LstmEnsemble(AiTraderModel):

    def create(self):
        x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train = self.scaled()
        model = self.modeling()
        self.training(model, x1_train_scaled, x2_train_scaled, y1_train)
        self.test(model, x1_test_scaled, x2_test_scaled, y1_test)
        self.save(model)

    def save(self, model):
        file_name = os.path.join(dir_path("aitrader"), "save", H5FileNames.lstm_ensemble.value)
        model.save(file_name)

    def test(self, model, x1_test_scaled, x2_test_scaled, y1_test):
        x1_test_scaled = x1_test_scaled.astype(np.float32)
        x2_test_scaled = x2_test_scaled.astype(np.float32)
        y1_test = y1_test.astype(np.float32)
        loss, mse = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)
        print(f"loss : {loss}\n"
              f"mse : {mse}")
        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])
        for i in range(5):
            print(f"종가 : {y1_test[i]} / 예측가 : {y1_pred[i]}")

    def training(self, model, x1_train_scaled, x2_train_scaled, y1_train):
        early_stopping = EarlyStopping(patience=20)
        x1_train_scaled = x1_train_scaled.astype(np.float32)
        x2_train_scaled = x2_train_scaled.astype(np.float32)
        y1_train = y1_train.astype(np.float32)
        model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2,
                  verbose=1, batch_size=1, epochs=100, callbacks=[early_stopping])

    def modeling(self):
        input1 = Input(shape=(5, 5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)
        input2 = Input(shape=(5, 5))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)
        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        return model

    def scaled(self):
        x1, y1 = self.split_xy5(samsung, 5, 1)
        x2, y2 = self.split_xy5(kospi200, 5, 1)
        x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=1, test_size=0.3)
        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=2, test_size=0.3)
        x1_train = np.reshape(x1_train, (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
        x1_test = np.reshape(x1_test, (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))
        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))

        scaler1 = StandardScaler()
        scaler1.fit(x1_train)
        x1_train_scaled = scaler1.transform(x1_train)
        x1_test_scaled = scaler1.transform(x1_test)
        scaler2 = StandardScaler()
        scaler2.fit(x2_train)
        x2_train_scaled = scaler2.transform(x2_train)
        x2_test_scaled = scaler2.transform(x2_test)

        x1_train_scaled = np.reshape(x1_train_scaled, (x1_train_scaled.shape[0], 5, 5))
        x1_test_scaled = np.reshape(x1_test_scaled, (x1_test_scaled.shape[0], 5, 5))
        x2_train_scaled = np.reshape(x2_train_scaled, (x2_train_scaled.shape[0], 5, 5))
        x2_test_scaled = np.reshape(x2_test_scaled, (x2_test_scaled.shape[0], 5, 5))
        return x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train
