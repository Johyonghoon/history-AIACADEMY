import pickle
import string
import folium
import googlemaps
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import json

pd.set_option('mode.chained_assignment', None)  # 경고 off


CRIME_MENUS = ["Exit",  # 0
               "Spec",  # 1
               "Save Police Position",  # 2
               "Save CCTV Population",  # 3
               "Save Police Norminalization",  # 4
               "Save US Folium",  # 5
               "Save Seoul Folium",  # 6
               "Partition",  # 7
               "미완성 : Fit",  # 8
               "미완성 : Predict"  # 9
               ]

crime_menu = {"1": lambda t: t.spec(),
              "2": lambda t: t.save_police_pos(),
              "3": lambda t: t.save_cctv_pop(),
              "4": lambda t: t.save_police_norm(),
              "5": lambda t: t.save_us_folium(),
              "6": lambda t: t.save_seoul_folium(),
              "7": lambda t: t.target(),
              "8": lambda t: t.partition(),
              "9": lambda t: t.which_cty_in_suv_compact(),
              "10": lambda t: t.find_top5_hwy_in_audi(),
              "11": lambda t: t.find_top3_avg(),
              }

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


class CrimeService:

    def __init__(self):
        self.crime = pd.read_csv('./../../../../static/data/dam/per/crime/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./../../../../static/data/dam/per/crime/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./../../../../static/titanic/dam/per/crime/pop_in_seoul.xls',
                                 usecols=['자치구', '합계', '한국인', '등록외국인', '65세이상고령자'], skiprows=[0, 2, 29])
        self.us_unemployment = pd.read_csv('./../../../../static/data/dam/per/crime/us_unemployment.csv')
        set_json_from_df("./../../../../static/titanic/dam/per/crime/us-states.json")
        self.us_states = "./../../../../static/titanic/dam/per/crime/us-states.json"
        self.kr_states = "./../../../../static/titanic/dam/per/crime/kr-state.json"

        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)  # regex=True
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']

    '''
    1.스펙보기 
    id = SERIALNO  
    Crime Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', 
           '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거'], dtype='object')
    CCTV Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object'
    '''

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

    def save_police_pos(self):  # 2
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f" 서울시내 경찰서는 총 {len(station_names)}개 이다")
        [print(f"{str(i)}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("### 키 입력 ###")
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
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '강서구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'

        crime.to_pickle("./../../../../static/save/dam/per/crime/police_pos.pkl")
        print(pd.read_pickle("./../../../../static/save/dam/per/crime/police_pos.pkl"))

    def save_cctv_pop(self):  # 3 ratio -> norminal
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
        }, inplace=True)
        pop['외국인비율'] = pop['외국인'] / pop['인구수'] * 100
        pop['고령자비율'] = pop['고령자'] / pop['인구수'] * 100
        cctv.drop(["2013년도 이전", "2014년", "2015년", "2016년"], axis=1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구별")

        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
        """
        cctv_pop.to_pickle("./../../../../static/save/dam/per/crime/cctv_pop.pkl")
        print(pd.read_pickle("./../../../../static/save/dam/per/crime/cctv_pop.pkl"))
    """
    타깃변수(=종속변수 dependant, y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: 검거율 현황
    타깃변수값: 
    """

    def save_police_norm(self):  # 4
        police_pos = pd.read_pickle('./../../../../static/save/dam/per/crime/police_pos.pkl')
        police = pd.pivot_table(police_pos, index="구별", aggfunc=np.sum)
        police['살인검거율'] = (police['살인 검거'].astype(int) / police['살인 발생'].astype(int)) * 100
        police['강도검거율'] = (police['강도 검거'].astype(int) / police['강도 발생'].astype(int)) * 100
        police['강간검거율'] = (police['강간 검거'].astype(int) / police['강간 발생'].astype(int)) * 100
        police['절도검거율'] = (police['절도 검거'].astype(int) / police['절도 발생'].astype(int)) * 100
        police['폭력검거율'] = (police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int)) * 100
        police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1, inplace=True)
        for i in self.crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100  # 데이터 값의 기간 오류로 100을 넘기는 것을 필터링
        police.rename(columns={'살인 발생': '살인',
                               '강도 발생': '강도',
                               '강간 발생': '강간',
                               '절도 발생': '절도',
                               '폭력 발생': '폭력'}, inplace=True)
        x = police[self.crime_rate_columns].values
        min_max_scalar = preprocessing.MinMaxScaler()
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        police_norm.to_pickle('./../../../../static/save/dam/per/crime/police_norm.pkl')
        print(pd.read_pickle('./../../../../static/save/dam/per/crime/police_norm.pkl'))

    def save_us_folium(self):   # 5
        geo_data = self.us_states
        data = self.us_unemployment
        bins = list(data["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        map = folium.Map(location=[48, -102], zoom_start=5)
        folium.Choropleth(
            geo_data=geo_data,  # us_states,
            data=data,  # us_unemployment,
            name="choropleth",
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Unemployment Rate (%)',
            bins=bins
        ).add_to(map)
        map.save("./../../../../static/save/dam/per/crime/unemployment.html")

    def save_seoul_folium(self):    # 6
        geo_data = self.kr_states
        data = self.create_folium_data()
        print(type(data))
        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        folium.Choropleth(
            geo_data=geo_data,  # us_states,
            data=data,  # us_unemployment,
            name="choropleth",
            columns=["State", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Crime Rate (%)'
        ).add_to(map)
        map.save("./../../../../static/save/dam/per/crime/seoul_crime.html")

    def create_folium_data(self):
        crime = self.crime
        police_pos = pd.read_pickle('./../../../../static/save/dam/per/crime/police_pos.pkl')
        police_norm = pd.read_pickle('./../../../../static/save/dam/per/crime/police_norm.pkl')
        temp = police_pos[self.arrest_columns] / police_pos[self.arrest_columns].max()
        police_pos['검거'] = np.sum(temp, axis=1)
        return tuple(zip(police_norm.index, police_norm['범죄']))

    def partition(self):
        pass


def set_json_from_df(fname):  # 미국 주가 콜롬비아, 푸에르토-리코(준주) 포함시
    df = pd.read_json(fname)
    df.drop(df.index[[8, 51]], inplace=True)
    df.to_json("./../../../../static/save/dam/per/crime/us-states.json", orient='index')


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = CrimeService()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            crime_menu[menu](t)
