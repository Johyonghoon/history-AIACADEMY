import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
Data columns (total 28 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   PID                   437 non-null    int64  
 1   county                437 non-null    object 
 2   state                 437 non-null    object 
 3   area                  437 non-null    float64
 4   poptotal              437 non-null    int64  
 5   popdensity            437 non-null    float64
 6   popwhite              437 non-null    int64  
 7   popblack              437 non-null    int64  
 8   popamerindian         437 non-null    int64  
 9   popasian              437 non-null    int64  
 10  popother              437 non-null    int64  
 11  percwhite             437 non-null    float64
 12  percblack             437 non-null    float64
 13  percamerindan         437 non-null    float64
 14  percasian             437 non-null    float64
 15  percother             437 non-null    float64
 16  popadults             437 non-null    int64  
 17  perchsd               437 non-null    float64
 18  percollege            437 non-null    float64
 19  percprof              437 non-null    float64
 20  poppovertyknown       437 non-null    int64  
 21  percpovertyknown      437 non-null    float64
 22  percbelowpoverty      437 non-null    float64
 23  percchildbelowpovert  437 non-null    float64
 24  percadultpoverty      437 non-null    float64
 25  percelderlypoverty    437 non-null    float64
 26  inmetro               437 non-null    int64  
 27  category              437 non-null    object 
dtypes: float64(15), int64(10), object(3)
"""

MENUS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]


def midwest_menu(MENUS):
    for i, j in enumerate(MENUS):
        print(f"{i}. {j}")
    return input("메뉴 입력 : ")


class MidwestController:

    def __init__(self):
        self.midwest = pd.read_csv("data/midwest.csv")

    def print_meta_data(self):      # No.1
        self.midwest.info()
        # print(self.midwest.info())

    def change_meta(self):          # No.2
        self.my_midwest = self.midwest.rename(columns={"poptotal":"total","popasian":"asian"})
        # print(self.my_midwest)

    def create_percentage(self):    # No.3
        self.change_meta()
        my_midwest = self.my_midwest
        my_midwest['asian_percentage'] = (my_midwest['asian'] / my_midwest['total']) * 100
        self.my_midwest = my_midwest
        # print(self.my_midwest)

    def asian_classify(self):       # No.4
        self.create_percentage()
        my_midwest = self.my_midwest
        asian_per = my_midwest['asian_percentage']
        asian_per_avg = asian_per.mean()
        my_midwest['asian_scale'] = np.where(asian_per >= asian_per_avg, 'large', 'small')
        self.my_midwest = my_midwest
        # print(f"### 아시아 인구 평균 : {asian_per_avg}")
        # print(my_midwest.tail())

    def draw_freq_bar_graph(self):  # No.5
        self.asian_classify()
        my_midwest = self.my_midwest
        self.count_test = my_midwest['asian_scale'].value_counts()
        self.count_test.plot.bar(rot=0)
        plt.savefig('./save/draw_freq_bar_graph_asian_scale')


if __name__ == '__main__':
    api = MidwestController()
    while True:
        menu = midwest_menu(MENUS)
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("메타데이터 출력")
            api.print_meta_data()
        elif menu == "2":
            print("poptotal/popasian 변수를 total/asian로 이름변경")
            api.change_meta()
        elif menu == "3":
            print("전체 인구 대비 아시아 인구 백분율 변수 추가")
            api.create_percentage()
        elif menu == "4":
            print("아시아 인구 백분율 전체 평균을 large/small 로 분류")
            api.asian_classify()
        elif menu == "5":
            print("large/small 빈도표와 빈도막대그래프 작성")
            api.draw_freq_bar_graph()
