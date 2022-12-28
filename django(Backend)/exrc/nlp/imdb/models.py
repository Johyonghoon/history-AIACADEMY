import numpy as np
import tensorflow as tf
from keras import Sequential
from keras.datasets import imdb
from keras.utils import pad_sequences
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from tensorflow import keras

tf.keras.utils.set_random_seed(42)
tf.config.experimental.enable_op_determinism()


class Imdb_model:
    def __init__(self):
        global raw_train_input, raw_train_target, raw_test_input, raw_test_target
        keras.utils.set_random_seed(42)
        tf.config.experimental.enable_op_determinism()
        (raw_train_input, raw_train_target), (raw_test_input, raw_test_target) = imdb.load_data(num_words=500)

    def model_hook(self):
        self.check_set()
        self.preprocess()
        self.create_rnn_model()
        self.fit()

    def print_review_info(self):
        print(raw_train_input.shape, raw_test_input.shape)
        print(f"첫 번째 리뷰의 길이 : {len(raw_train_input[0])}")
        print(f"두 번째 리뷰의 길이 : {len(raw_train_input[1])}")
        print(f"첫 번째 리뷰의 내용 : {raw_train_input[0]}")
        print(f"타깃 데이터(부정과 긍정) : {raw_train_target[:20]}")

    def check_set(self):
        global train_input, val_input, train_target, val_target
        train_input, val_input, train_target, val_target = train_test_split(raw_train_input, raw_train_target,
                                                                            test_size=0.2, random_state=42)
        lengths = np.array([len(x) for x in train_input])
        # print(np.mean(lengths), np.median(lengths))

        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('frequency')
        plt.show()

    def preprocess(self):
        global train_seq, val_seq
        train_seq = pad_sequences(train_input, maxlen=100)
        # print(train_seq.shape)
        # print(train_seq[0])
        # print(train_input[0][-10:])
        # print(train_seq[5])
        val_seq = pad_sequences(val_input, maxlen=100)

    def create_rnn_model(self):
        global train_oh, val_oh, model
        model = keras.Sequential()
        sample_length = 100
        freq_words = 500
        model.add(keras.layers.SimpleRNN(8, input_shape=(sample_length, freq_words)))
        model.add(keras.layers.Dense(1, activation='sigmoid'))
        train_oh = keras.utils.to_categorical(train_seq)    # oh is one-hot encoding
        # print(train_oh.shape)
        # print(train_oh[0][0][:12])
        # print(np.sum(train_oh[0][0]))
        val_oh = keras.utils.to_categorical(val_seq)
        # model.summary()
        return model

    def fit(self):
        rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
        model = self.create_rnn_model()
        model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
        checkpoint_cb = keras.callbacks.ModelCheckpoint('data/best-simplernn-model.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
                            validation_data=(val_oh, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train', 'val'])
        plt.show()


if __name__ == '__main__':
    model = Imdb_model()
    model.model_hook()
