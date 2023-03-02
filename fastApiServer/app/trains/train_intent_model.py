# 필요한 모듈 임포트
import os

import pandas as pd
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate
from keras.utils import pad_sequences

from app.admin.path import dir_path
from app.configs.chatbot.global_params import MAX_SEQ_LEN
from app.utils.chatbot.preprocess import Preprocess


class TrainIntentModel:

    def __init__(self):
        train_file = os.path.join(dir_path("trains"), "data", "intent", "total_train_data.csv")
        data = pd.read_csv(train_file, delimiter=',')
        self.queries = data['query'].tolist()
        self.intents = data['intent'].tolist()
        os.path.join(dir_path("trains"), "data", "user_dic.tsv")
        self.p = Preprocess(word2index_dic=os.path.join(dir_path("trains"), "data", "chatbot_dict.bin"),
                            userdic=os.path.join(dir_path("trains"), "data", "user_dic.tsv"))
        self.sequences = []
        self.padded_seqs = None

        # 하이퍼 파라미터 설정
        self.dropout_prob = 0.5
        self.EMB_SIZE = 128
        self.EPOCH = 5
        self.VOCAB_SIZE = len(self.p.word_index) + 1  # 전체 단어 개수

        self.train_ds = None
        self.val_ds = None
        self.test_ds = None

        self.pool1 = None
        self.pool2 = None
        self.pool3 = None
        self.input_layer = None
        self.predictions = None
        self.model = None

    def hook(self):
        self.create_sequence()
        self.dataset()
        self.cnn_model()
        self.modeling()
        self.evaluate()
        self.save()

    # 단어 시퀀스 생성
    def create_sequence(self):
        for sentence in self.queries:
            pos = self.p.pos(sentence)
            keywords = self.p.get_keywords(pos, without_tag=True)
            seq = self.p.get_wordidx_sequence(keywords)
            self.sequences.append(seq)

        # 단어 인덱스 시퀀스 벡터 ○2
        # 단어 시퀀스 벡터 크기
        self.padded_seqs = pad_sequences(self.sequences, maxlen=MAX_SEQ_LEN, padding='post')

        # (105658, 15)
        print(self.padded_seqs.shape)
        print(len(self.intents))  # 105658

    # 학습용, 검증용, 테스트용 데이터셋 생성 ○3
    # 학습셋:검증셋:테스트셋 = 7:2:1
    def dataset(self):
        ds = tf.data.Dataset.from_tensor_slices((self.padded_seqs, self.intents))
        ds = ds.shuffle(len(self.queries))

        train_size = int(len(self.padded_seqs) * 0.7)
        val_size = int(len(self.padded_seqs) * 0.2)
        test_size = int(len(self.padded_seqs) * 0.1)

        self.train_ds = ds.take(train_size).batch(20)
        self.val_ds = ds.skip(train_size).take(val_size).batch(20)
        self.test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

    # CNN 모델 정의  ○4
    def cnn_model(self):
        self.input_layer = Input(shape=(MAX_SEQ_LEN,))
        embedding_layer = Embedding(self.VOCAB_SIZE, self.EMB_SIZE, input_length=MAX_SEQ_LEN)(self.input_layer)
        dropout_emb = Dropout(rate=self.dropout_prob)(embedding_layer)

        conv1 = Conv1D(
            filters=128,
            kernel_size=3,
            padding='valid',
            activation=tf.nn.relu)(dropout_emb)
        self.pool1 = GlobalMaxPool1D()(conv1)

        conv2 = Conv1D(
            filters=128,
            kernel_size=4,
            padding='valid',
            activation=tf.nn.relu)(dropout_emb)
        self.pool2 = GlobalMaxPool1D()(conv2)

        conv3 = Conv1D(
            filters=128,
            kernel_size=5,
            padding='valid',
            activation=tf.nn.relu)(dropout_emb)
        self.pool3 = GlobalMaxPool1D()(conv3)

        # 3,4,5gram 이후 합치기
        concat = concatenate([self.pool1, self.pool2, self.pool3])

        hidden = Dense(128, activation=tf.nn.relu)(concat)
        dropout_hidden = Dropout(rate=self.dropout_prob)(hidden)
        logits = Dense(5, name='logits')(dropout_hidden)
        self.predictions = Dense(5, activation=tf.nn.softmax)(logits)

    def modeling(self):

        # 모델 생성  ○5
        self.model = Model(inputs=self.input_layer, outputs=self.predictions)
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

        # 모델 학습 ○6
        self.model.fit(self.train_ds, validation_data=self.val_ds, epochs=self.EPOCH, verbose=1)

    # 모델 평가(테스트 데이터 셋 이용) ○7
    def evaluate(self):
        loss, accuracy = self.model.evaluate(self.test_ds, verbose=1)
        print('Accuracy: %f' % (accuracy * 100))
        print('loss: %f' % loss)

    # 모델 저장  ○8
    def save(self):
        self.model.save(os.path.join(dir_path("models"), "chatbot", "intent.h5"))


if __name__ == '__main__':
    TrainIntentModel().hook()
    