import googlemaps
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

pd.set_option('mode.chained_assignment', None) # 경고 off


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')

CRIME_MENUS = ["Exit", # 0
               "Spec", # 1
               "Merge", # 2 여러 개의 객체를 하나로 통합
               "Inteval", # 3
               "Norminal", # 4
               "Target", # 5
               "Partition", # 6
               "미완성 : Fit", # 7
               "미완성 : Predict" # 8
                ]

"""
 --- 3.Info ---
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   관서명     31 non-null     object
 1   살인 발생   31 non-null     int64 
 2   살인 검거   31 non-null     int64 
 3   강도 발생   31 non-null     int64 
 4   강도 검거   31 non-null     int64 
 5   강간 발생   31 non-null     int64 
 6   강간 검거   31 non-null     int64 
 7   절도 발생   31 non-null     object
 8   절도 검거   31 non-null     object
 9   폭력 발생   31 non-null     object
 10  폭력 검거   31 non-null     object
dtypes: int64(6), object(5)
memory usage: 2.8+ KB
"""


crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.interval(),
    "4" : lambda t: t.norminal(),
    "5" : lambda t: t.target(),
    "6" : lambda t: t.partition(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}


class CrimeService:

    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.my_crime = None
        self.my_cctv = None

    def spec(self):
        def print_spec(x):
            print(f" --- 1.Shape --- \n{x.shape}\n"
                  f" --- 2.Features --- \n{x.columns}\n"
                  f" --- 3.Info --- \n{x.info()}\n"
                  f" --- 4.Case Top1 --- \n{x.head(1)}\n"
                  f" --- 5.Case Bottom1 --- \n{x.tail(3)}\n"
                  f" --- 6.Describe --- \n{x.describe()}\n"
                  f" --- 7.Describe All --- \n{x.describe(include='all')}\n")
        print_spec(self.crime)
        print_spec(self.cctv)

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역이름: {name}")
            station_names.append(f"서울{str(name[:-1])}경찰서")
        print(f"서울시내 경찰서는 총 {len(station_names)}이다.")
        print([f"서울{str(i)}경찰서" for i in station_names])
        print(" ### API에서 주소 추출 시작")
        """
        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print("### API에서 주소 추출 시작 ###")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f"name {i} = {_[0].get('formatted_address')}")
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)

        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv', index=False)
        """
        pop = pd.read_excel('./data/pop_in_seoul.xls', header=1, usecols=[1, 3, 6, 9, 13], skiprows=[2])
        print(pop.head())

    '''
     --- 2.Features ---
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
           '절도 검거', '폭력 발생', '폭력 검거']

    '''
    '''
    타깃변수(=종속변수 dependant, y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: 검거율 현황
    타깃변수값: 
    '''

    def interval(self):
        pass

    def ratio(self):
        pass

    def norminal(self):
        pass

    def ordinal(self):
        pass

    def target(self):
        pass

    def partition(self):
        pass


if __name__ == '__main__':
    t = CrimeService()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            crime_menu[menu](t)
