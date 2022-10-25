from dataclasses import dataclass


@dataclass
class Dataset(object):

    context: str    #파일 저장경로
    fname: str      #파일 이름
    train: object   #train.csv 가 데이터프레임으로 전환된 객체(읽어들여야 할 파일)
    test: object    #train.csv 가 데이터프레임으로 전환된 객체(읽어들여야 할 파일)
    id: str         #탑승자 승선번호(문제)
    label: str      #탑승자 승선번호에 따른 생존여부(정답)

    # 데이터를 읽고(getter = property) / 쓰기(setter) 기능을 추가한다.