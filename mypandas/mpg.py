import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64  
 1   manufacturer : 회사  234 non-null    object 
 2   model : 모델        234 non-null    object 
 3   displ : 배기량        234 non-null    float64
 4   year : 연식         234 non-null    int64  
 5   cyl : 실린더          234 non-null    int64  
 6   trans : 차축        234 non-null    object 
 7   drv : 오토          234 non-null    object 
 8   cty : 시내연비          234 non-null    int64  
 9   hwy : 시외연비          234 non-null    int64  
 10  fl : 연료           234 non-null    object 
 11  class : 차종        234 non-null    object 
dtypes: float64(1), int64(5), object(6)
"""
change_meta = {"manufacturer" : "회사",
               "model" : "모델",
               "displ" : "배기량",
               "year" : "연식",
               "cyl" : "실린더",
               "trans" : "차축",
               "drv" : "오토",
               "cty" : "시내연비",
               "hwy" : "시외연비",
               "fl" : "연료",
               "class" : "차종"}

MENUS = ['종료', 'mpg 앞부분 확인', 'mpg 뒷부분 확인', '행,열 출력', '데이터 속성 확인',
         '요약 통계량 출력', '문자 변수 요약 통계량 함께 출력', 'manufacturer를 company로 변경',
         'test 변수 생성', 'test 빈도표 만들기', 'test 빈도 막대 그래프 그리기',
         # test 변수 생성 : cty와 hwy 변수를 머지(merge)하여 total 변수 생성하고 20 이상이면 pass, 미만이면 fail 저장
         'displ(배기량)이 4 이하와 5 이상 자동차의 hwy(고속도로 연비) 비교',
         '아우디와 도요타 중 도시연비(cty) 평균이 높은 회사 검색',
         '쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균',
         # mpg 150페이지 문제
         # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
         # 후 다음 문제 풀이
         'suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?',
         # mpg 153p 문제
         '아우디 차에서 고속도로 연비 1~5위 출력하시오/'
         # mpg 158p 문제
         '평균연비가 가장 높은 자동차 1~3위 출력하시오.']


def mpg_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i} : {j}")
    return input("메뉴 선택 : ")


class MpgController:

    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')
        self.my_mpg = None

    def head(self): # No.1
        print(self.mpg.head())

    def tail(self): # No.2
        print(self.mpg.tail())

    def shape(self): # No.3
        print(self.mpg.shape)

    def info(self): # No.4
        print(self.mpg.info())

    def describe(self): # No.5
        print(self.mpg.describe())

    def describe_include(self): # No.6
        print(self.mpg.describe(include='all'))

    def change_meta(self): # No.7
        self.my_mpg = self.mpg.rename(columns=change_meta)

    def create_test_variable(self): # No.8
        self.change_meta()
        t = self.my_mpg
        t['평균연비'] = (t['시내연비'] + t['시외연비']) / 2
        t['연비테스트'] = np.where(t['평균연비'] >= 20, 'pass', 'fail')
        self.my_mpg = t

    def create_test_frequency(self): # No.9
        self.create_test_variable()
        t = self.my_mpg
        self.count_test = t['연비테스트'].value_counts()
        print(self.count_test)

    def draw_freq_bar_graph(self): # No.10
        self.create_test_frequency()
        self.count_test.plot.bar(rot=0)
        plt.savefig('./save/draw_freq_bar_graph.png')

    def compare_displ_and_hwy(self): # No.11
        self.change_meta()
        df_low_displ_avg_hwy = self.my_mpg.query("배기량 <= 4")["시외연비"].mean()
        df_high_displ_avg_hwy = self.my_mpg.query("배기량 >= 5")["시외연비"].mean()
        print(f'배기량 4 이하 차량의 시외연비 : {df_low_displ_avg_hwy}')
        print(f'배기량 5 이상 차량의 시외연비 : {df_high_displ_avg_hwy}')
        if df_low_displ_avg_hwy > df_high_displ_avg_hwy:
            print("따라서, 배기량이 적은 차량이 평균 시외연비가 더 좋다.")
        elif df_low_displ_avg_hwy < df_high_displ_avg_hwy:
            print("따라서, 배기량이 많은 차량이 평균 시외연비가 더 좋다.")

    def search_higher_cty(self): # No.12
        self.change_meta()
        df_audi = self.my_mpg.query("회사 == 'audi'")["시내연비"].mean()
        df_toyota = self.my_mpg.query("회사 == 'toyota'")["시내연비"].mean()
        print(f'아우디 시내연비 : {df_audi}')
        print(f'도요타 시내연비 : {df_toyota}')
        if df_audi > df_toyota:
            print("따라서, 아우디가 도요타보다 평균 시내연비가 더 좋다.")
        elif df_audi < df_toyota:
            print("따라서, 도요타가 아우디보다 평균 시내연비가 더 좋다.")

    def find_hwy_average(self): # No.13
        self.change_meta()
        df_three = self.my_mpg.query('회사 == "chevrolet" | 회사 == "ford" | 회사 == "honda"')
        print(df_three)
        print(f'쉐보레/포드/혼다의 평균 시외연비 : {df_three["시외연비"].mean()}')

    def which_higher_between_suv_compact(self): # No.14
        self.change_meta()
        df_suv = self.my_mpg.query("차종 == 'suv'")["시내연비"].mean()
        df_compact = self.my_mpg.query("차종 == 'compact'")["시내연비"].mean()
        print(f'suv 시내연비 : {df_suv}')
        print(f'compact 시내연비 : {df_compact}')
        if df_suv > df_compact:
            print("따라서, suv가 compact보다 평균 시내연비가 더 좋다.")
        elif df_suv < df_compact:
            print("따라서, compact가 suv보다 평균 시내연비가 더 좋다.")


    def search_hwy_in_audi_top5(self): # No.15
        self.change_meta()
        df_audi = self.my_mpg.query("회사 == 'audi'")
        print(df_audi.sort_values('시외연비', ascending=False)[['회사', '모델', '오토', '차종', '시외연비']].head())

    def search_average_mileage_top3(self): # No.16
        self.create_test_variable()
        print(self.my_mpg.sort_values('평균연비', ascending=False)[['회사', '모델', '오토', '차종', '평균연비']].head(3))


if __name__ == '__main__':
    api = MpgController()
    while True:
        menu = mpg_menu(MENUS)
        if menu == '0':
            print(MENUS[0])
            break
        elif menu == '1':
            print(MENUS[1])
            api.head()
        elif menu == '2':
            print(MENUS[2])
            api.tail()
        elif menu == '3':
            print(MENUS[3])
            api.shape()
        elif menu == '4':
            print(MENUS[4])
            api.info()
        elif menu == '5':
            print(MENUS[5])
            api.describe()
        elif menu == '6':
            print(MENUS[6])
            api.describe_include()
        elif menu == '7':
            print(MENUS[7])
        elif menu == '8':
            print(MENUS[8])
            api.create_test_variable()
        elif menu == '9':
            print(MENUS[9])
            api.create_test_frequency()
        elif menu == '10':
            print(MENUS[10])
            api.draw_freq_bar_graph()
        elif menu == '11':
            # mpg 144페이지 문제
            print("displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교")
            api.compare_displ_and_hwy()
        elif menu == '12':
            print("아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색")
            api.search_higher_cty()
        elif menu == '13':
            print("쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균")
            api.find_hwy_average()
        elif menu == '14':
            # mpg 150페이지 문제
            # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
            # 후 다음 문제 풀이
            print("suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?")
            api.which_higher_between_suv_compact()
        elif menu == '15':
            print("아우디차에서 고속도로 연비 1~5위 출력하시오")
            api.search_hwy_in_audi_top5()
        elif menu == '16':
            print("평균연비가 가장 높은 자동차 1~3위 출력하시오")
            api.search_average_mileage_top3()
        else:
            print("잘못된 번호입니다")

