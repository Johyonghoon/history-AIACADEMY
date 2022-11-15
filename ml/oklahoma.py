import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

pd.set_option('mode.chained_assignment', None) # 경고 off


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')

OKLAHOMA_MENUS = ["Exit", # 0
                  "Spec", # 1
                  "rename", # 2
                  "Inteval", # 3
                  "Norminal", # 4
                  "Target", # 5
                  "Partition", # 6
                  "미완성 : Fit", # 7
                  "미완성 : Predict" # 8
                  ]

oklahoma_meta = {'AGEP' : '나이', 'BDSP' : '침실 수', 'CONP' : '월 수선비',
                 'ELEP' : '월 전기료', 'GASP' : '월 가스비', 'HINCP' : '가계 소득',
                 'MAR' : '결혼 상태', 'NRC' : '자녀 수', 'RMSP' : '방 수',
                 'VALP' : '주택 가격', 'VALP_B1' : '주택 가격비교'
                 }

"""
RangeIndex: 21395 entries, 0 to 21394
Data columns (total 32 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   ACCESS   21395 non-null  float64
 1   ACR      21395 non-null  float64
 2   AGEP     21395 non-null  int64  
 3   BATH     21395 non-null  float64
 4   BDSP     21395 non-null  float64
 5   BLD      21395 non-null  float64
 6   CONP     21395 non-null  float64
 7   COW      12111 non-null  float64
 8   ELEP     21395 non-null  float64
 9   FESRP    21395 non-null  int64  
 10  FKITP    21395 non-null  float64
 11  FPARC    18744 non-null  float64
 12  FSCHP    21395 non-null  int64  
 13  FTAXP    21395 non-null  float64
 14  GASP     21395 non-null  float64
 15  HHL      21395 non-null  float64
 16  HHT      21395 non-null  float64
 17  HINCP    21395 non-null  float64
 18  LANX     20330 non-null  float64
 19  MAR      21395 non-null  int64  
 20  MV       21395 non-null  float64
 21  NRC      21395 non-null  float64
 22  R18      21395 non-null  float64
 23  R65      21395 non-null  float64
 24  RAC1P    21395 non-null  int64  
 25  RMSP     21395 non-null  float64
 26  RWAT     21395 non-null  float64
 27  SCH      20760 non-null  float64
 28  SCHL     20760 non-null  float64
 29  SEX      21395 non-null  int64  
 30  VALP     21395 non-null  float64
 31  VALP_B1  21395 non-null  float64
dtypes: float64(26), int64(6)
"""

oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval(),
    "4" : lambda t: t.norminal(),
    "5" : lambda t: t.target(),
    "6" : lambda t: t.partition(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}


class OklahomaService:
    def __init__(self):
        self.oklahoma = pd.read_csv('./data/comb32.csv')
        self.my_oklahoma = None
    '''
    1.스펙 보기
    '''
    def spec(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(self.oklahoma.shape)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)
        print(" --- 3.Info ---")
        print(self.oklahoma.info())
        print(" --- 4.Case Top1 ---")
        print(self.oklahoma.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.oklahoma.tail(3))
        print(" --- 6.Describe ---")
        print(self.oklahoma.describe())
        print(" --- 7.Describe All ---")
        print(self.oklahoma.describe(include='all'))
    '''
    2.한글 메타데이터
     --- 2.Features ---
    Index(['아이디', '성별', '나이', '고혈압', '심장병', '기혼여부', 
            '직종', '거주형태', '평균혈당', '비만도', '흡연여부', '뇌졸중'],

    '''
    def rename_meta(self):
        self.my_oklahoma = self.oklahoma.rename(columns=oklahoma_meta)
        print(" --- 2.Features ---")
        print(self.my_oklahoma.columns)

    '''
    타깃변수(=종속변수 dependant, y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: VALP_B1 (=주택 가격비교)
    타깃변수값: 주택 가격 중위수 이상 1, 아니면 0
    '''
    """
    3. 연속형 = ['나이', '침실 수', '월 수선비', '월 전기료', '월 가스비',
                '가계 소득', '자녀 수', '방 수', '주택 가격']
    """
    def interval(self):
        self.rename_meta()
        df = self.my_oklahoma
        cols_interval = ['나이', '침실 수', '월 수선비', '월 전기료', '월 가스비',
                         '가계 소득', '자녀 수', '방 수', '주택 가격']
        print(f"--- 구간변수 타입 ---\n {df[cols_interval].dtypes}")
        print(f"--- 결측값 있는 변수 ---\n {df[cols_interval].isna().any()[lambda x: x]}") # 결측값이 없음
        print(f"--- 월 수선비 분포 확인--- \n {df['월 수선비'].value_counts(normalize=True)}")
        # 월 수선비 지출이 없는 집단 : 99.6%로 unary 변수이므로 분석에서 제외
        df.drop(['월 수선비'], axis=1, inplace=True)
        print(f"--- '월 수선비' 제거한 스펙 --- \n{df.shape}")
        self.my_oklahoma_except_conp = df
        # 월 전기료, 월 가스비, 가계 소득의 최댓값이 상한을 초과하는 값을 이상치로 규정하고 제거
        df = self.my_oklahoma_except_conp
        c1 = df['월 전기료'] <= 500
        c2 = df['월 가스비'] <= 311
        c3 = df['가계 소득'] <= 320000
        self.my_oklahoma_except_outlier = df[c1 & c2 & c3]
        cols_interval2 = ['나이', '침실 수', '월 전기료', '월 가스비',
                          '가계 소득', '자녀 수', '방 수', '주택 가격']
        print(f"--- 이상치 제거한 7개 구간변수 및 주택 가격 요약 통계 --- "
              f"\n{self.my_oklahoma_except_outlier[cols_interval2].describe()}")
        print(f"--- 이상치 제거한 주택 가격비교 분포 --- "
              f"\n{self.my_oklahoma_except_outlier['주택 가격비교'].value_counts(normalize=True)}")
        print(f"--- 이상치 제거한 스펙 --- \n{self.my_oklahoma_except_outlier.shape}")
        self.my_oklahoma_except_outlier.to_csv("./save/oklahoma_except_conp_and_outlier.csv")

    def ratio(self):  # 해당 컬럼 없음
        pass
    '''
    4. 범주형 = ['결혼 상태']
    '''
    def norminal(self):
        self.interval()
        df = self.my_oklahoma_except_outlier
        cols_norminal = ['결혼 상태']
        df['결혼 상태'].value_counts(dropna=False)
        print(f"--- 범주형 변수 타입 --- \n {df[cols_norminal].dtypes}")
        print(f"--- 타깃 변수값에 따른 범주형 변수 분표(분할표, 개수) --- "
              f"\n {pd.crosstab(df['결혼 상태'], df['주택 가격비교'])}")
        print(f"--- 타깃 변수값에 따른 범주형 변수 분표(분할표, 비율) --- "
              f"\n {pd.crosstab(df['결혼 상태'], df['주택 가격비교'], normalize=True)}")

        # 결측값 조치
        print(f"--- 이상치 제거한 데이터 스펙 타입 --- \n {df.dtypes}")
        print(f"--- 이상치 제거한 데이터 결측값 --- \n {df.isnull().sum()}")
        print(f"--- 이상치 제거한 데이터의 결측값 있는 변수 --- \n {df.isna().any()[lambda x: x]}")
        cols_null = ['COW', 'FPARC', 'LANX', 'SCH', 'SCHL']
        df[cols_null] = df[cols_null].fillna(0).astype(np.int64)
        df[cols_null].isnull().mean()

        # 타깃 변수 VALP를 제외한 변수를 저장
        self.oklahoma_with_VALP_B1 = df.drop(['주택 가격'], axis=1)
        print(self.oklahoma_with_VALP_B1.shape)
        print(" ### 프리프로세스 종료 ###")
        print(f"--- 타겟 변수 VALP 제거한 스펙 --- \n{self.oklahoma_with_VALP_B1.shape}")
        self.oklahoma_with_VALP_B1.to_csv("./save/oklahoma_var30.csv")

    def ordinal(self):   # 해당 컬럼 없음
        pass

    def target(self):
        df_var30 = pd.read_csv('./save/oklahoma_var30.csv')
        print(df_var30)
        data = df_var30.drop(['주택 가격비교'], axis=1)
        target = df_var30['주택 가격비교']
        print(data.shape)
        print(target.shape)
        return data, target

    def partition(self):
        data, target = self.target()
        X_train, X_test, y_train, y_test = train_test_split(data, target,
                                                            test_size=0.5, random_state=42, stratify=target)
        print("X_train shape:", X_train.shape)
        print("X_test shape:", X_test.shape)
        print("y_train shape:", y_train.shape)
        print("y_test shape:", y_test.shape)


if __name__ == '__main__':
    t = OklahomaService()
    while True:
        menu = my_menu(OKLAHOMA_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            oklahoma_menu[menu](t)
            """
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
            """