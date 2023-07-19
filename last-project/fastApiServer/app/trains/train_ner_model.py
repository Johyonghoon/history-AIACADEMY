import os

import tensorflow as tf
from keras import preprocessing
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Embedding, Dense, TimeDistributed,  Bidirectional
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from seqeval.metrics import f1_score, classification_report
import numpy as np

from app.admin.path import dir_path
from app.utils.chatbot.preprocess import Preprocess


class TrainNERModel:

    def __init__(self):
        self.p = Preprocess(word2index_dic=os.path.join(dir_path("trains"), "data", "chatbot_dict.bin"),
                            userdic=os.path.join(dir_path("trains"), "data", "user_dic.tsv"))
        self.sentences, self.tags = [], []

        self.index_to_ner = None
        self.vocab_size = None
        self.tag_size = None
        self.max_len = 40
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.model = None

    def hook(self):
        self.dataset()
        self.tokenizer()
        self.modeling()
        self.ner_predict()

    # 학습 파일 불러오기
    def read_file(self, file_name):
        sents = []
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for idx, l in enumerate(lines):
                if l[0] == ';' and lines[idx + 1][0] == '$':
                    this_sent = []
                elif l[0] == '$' and lines[idx - 1][0] == ';':
                    continue
                elif l[0] == '\n':
                    sents.append(this_sent)
                else:
                    this_sent.append(tuple(l.split()))
        return sents

    def dataset(self):
        # 학습용 말뭉치 데이터를 불러옴

        corpus = self.read_file(os.path.join(dir_path("trains"), "data", "ner", "ner_train.tx"))
        # 말뭉치 데이터에서 단어와 BIO 태그만 불러와 학습용 데이터셋 생성

        for t in corpus:
            tagged_sentence = []
            sentence, bio_tag = [], []
            for w in t:
                tagged_sentence.append((w[1], w[3]))
                sentence.append(w[1])
                bio_tag.append(w[3])

            self.sentences.append(sentence)
            self.tags.append(bio_tag)

        print("샘플 크기 : \n", len(self.sentences))
        print("0번 째 샘플 단어 시퀀스 : \n", self.sentences[0])
        print("0번 째 샘플 bio 태그 : \n", self.tags[0])
        print("샘플 단어 시퀀스 최대 길이 :", max(len(l) for l in self.sentences))
        print("샘플 단어 시퀀스 평균 길이 :", (sum(map(len, self.sentences))/len(self.sentences)))

    # 토크나이저 정의
    def tokenizer(self):
        tag_tokenizer = preprocessing.text.Tokenizer(lower=False)  # 태그 정보는 lower=False 소문자로 변환하지 않는다.
        tag_tokenizer.fit_on_texts(self.tags)

        # 단어사전 및 태그 사전 크기
        self.vocab_size = len(self.p.word_index) + 1
        self.tag_size = len(tag_tokenizer.word_index) + 1
        print("BIO 태그 사전 크기 :", self.tag_size)
        print("단어 사전 크기 :", self.vocab_size)

        # 학습용 단어 시퀀스 생성
        x_train = [self.p.get_wordidx_sequence(sent) for sent in self.sentences]
        y_train = tag_tokenizer.texts_to_sequences(self.tags)

        self.index_to_ner = tag_tokenizer.index_word  # 시퀀스 인덱스를 NER로 변환 하기 위해 사용
        self.index_to_ner[0] = 'PAD'

        x_train = pad_sequences(x_train, padding='post', maxlen=self.max_len)
        y_train = pad_sequences(y_train, padding='post', maxlen=self.max_len)

        # 학습 데이터와 테스트 데이터를 8:2의 비율로 분리
        x_train, x_test, y_train, y_test = train_test_split(x_train, y_train,
                                                            test_size=.2,
                                                            random_state=1234)

        # 출력 데이터를 one-hot encoding
        y_train = tf.keras.utils.to_categorical(y_train, num_classes=self.tag_size)
        y_test = tf.keras.utils.to_categorical(y_test, num_classes=self.tag_size)

        print("학습 샘플 시퀀스 형상 : ", x_train.shape)
        print("학습 샘플 레이블 형상 : ", y_train.shape)
        print("테스트 샘플 시퀀스 형상 : ", x_test.shape)
        print("테스트 샘플 레이블 형상 : ", y_test.shape)

        self.x_train, self.x_test, self.y_train, self.y_test = x_train, x_test, y_train, y_test

    def modeling(self):
        model = Sequential()
        model.add(Embedding(input_dim=self.vocab_size, output_dim=30, input_length=self.max_len, mask_zero=True))
        model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recurrent_dropout=0.25)))
        model.add(TimeDistributed(Dense(self.tag_size, activation='softmax')))
        model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
        model.fit(self.x_train, self.y_train, batch_size=128, epochs=10)
        print("평가 결과 : ", model.evaluate(self.x_test, self.y_test)[1])

        model.save(os.path.join(dir_path("models"), "chatbot", "chatbot"))
        self.model = model

    # 시퀀스를 NER 태그로 변환
    def sequences_to_tag(self, sequences):  # 예측값을 index_to_ner를 사용하여 태깅 정보로 변경하는 함수.
        result = []
        for sequence in sequences:  # 전체 시퀀스로부터 시퀀스를 하나씩 꺼낸다.
            temp = []
            for pred in sequence:  # 시퀀스로부터 예측값을 하나씩 꺼낸다.
                pred_index = np.argmax(pred)  # 예를 들어 [0, 0, 1, 0 ,0]라면 1의 인덱스인 2를 리턴한다.
                temp.append(self.index_to_ner[pred_index].replace("PAD", "O"))  # 'PAD'는 'O'로 변경
            result.append(temp)
        return result

    def ner_predict(self):
        # 테스트 데이터셋의 NER 예측
        y_predicted = self.model.predict(self.x_test)
        pred_tags = self.sequences_to_tag(y_predicted)  # 예측된 NER
        test_tags = self.sequences_to_tag(self.y_test)  # 실제 NER

        # F1 평가 결과
        print(classification_report(test_tags, pred_tags))
        print("F1-score: {:.1%}".format(f1_score(test_tags, pred_tags)))


if __name__ == '__main__':
    TrainNERModel().hook()
