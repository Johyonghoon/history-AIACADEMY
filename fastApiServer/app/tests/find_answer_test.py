# 챗봇 엔진 동작
import os

from app.admin.path import dir_path
from app.configs.chatbot.database import *

from app.models.chatbot.intent_model import IntentModel
from app.models.chatbot.ner_model import NerModel
from app.cruds.chatbot import Chatbot
from app.utils.chatbot.find_answer import FindAnswer
from app.utils.chatbot.preprocess import Preprocess


class FindAnswerTest:

    def process(self, request_data):
        # 전처리 객체 생성
        p = Preprocess(word2index_dic=os.path.join(dir_path("trains"), "data", "chatbot_dict.bin"),
                       userdic=os.path.join(dir_path("trains"), "data", "user_dic.tsv"))

        # 질문/답변 학습 디비 연결 객체 생성
        db = Chatbot(
            host=HOSTNAME,
            user=USERNAME,
            password=PASSWORD,
            db_name=DATABASE,
            charset=CHARSET
        )
        db.connect()    # 디비 연결

        # 원문
        #query = "오전에 탕수육 10개 주문합니다"
        query = request_data

        # 의도 파악

        intent = IntentModel(model_name=os.path.join(dir_path("models"), "chatbot", "intent_model.h5"), preprocess=p)
        predict = intent.predict_class(query)
        intent_name = intent.labels[predict]

        # 개체명 인식
        ner = NerModel(model_name=os.path.join(dir_path("models"), "chatbot", "ner_model.h5"), preprocess=p)
        predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        print("질문 : ", query)
        print("=" * 40)
        print("의도 파악 : ", intent_name)
        print("답변 검색에 필요한 NER 태그 : ", ner_tags)
        print("=" * 40)

        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(predicts, answer_text)
        except:
            answer = "죄송해요, 무슨 말인지 모르겠어요."

        print("답변 : ", answer)

        db.close()  # 디비 연결 끊음


if __name__ == '__main__':
    FindAnswerTest().process(request_data=input("음식을 주문해보세요"))
