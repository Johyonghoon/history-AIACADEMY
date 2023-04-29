import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

from utils import my_menu

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
                         115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
                         150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
                         218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
                         556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
                         850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
                         1000.0])


class MultipleReression:

    def __init__(self):
        global train_input, test_input, train_target, test_target
        df = pd.read_csv('https://bit.ly/perch_csv_data')
        perch_full = df.to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)

    def transformer(self):
        poly = PolynomialFeatures(include_bias=False)
        poly.fit(train_input)
        train_poly = poly.transform(train_input)
        test_poly = poly.transform(test_input)
        return poly, train_poly, test_poly

    def print_transformer_data(self):
        poly, train_poly, test_poly = self.transformer()
        print(f"Transform data : {train_poly}")
        print(f"Transform data's shape : {train_poly.shape}")
        print(f"Get feature names : {poly.get_feature_names_out()}")

    def lr_model(self, input, target):
        lr = LinearRegression()
        lr.fit(input, target)
        return lr

    def lr_test(self):
        poly, train_poly, test_poly = self.transformer()
        lr = self.lr_model(train_poly, train_target)
        train_score = lr.score(train_poly, train_target)
        test_score = lr.score(test_poly, test_target)
        print(f"LR's coefficient of determination about trainset : {train_score}")
        print(f"LR's coefficient of determination about testset : {test_score}")

    def lr_test_adding_feature(self):
        poly = PolynomialFeatures(degree=5, include_bias=False)
        poly.fit(train_input)
        train_poly = poly.transform(train_input)
        test_poly = poly.transform(test_input)
        print(f"Transform data's shape : {train_poly.shape}")

        lr = self.lr_model(train_poly, train_target)
        lr.fit(train_poly, train_target)
        train_score = lr.score(train_poly, train_target)
        test_score = lr.score(test_poly, test_target)
        print(f"LR's coefficient of determination about trainset : {train_score}")
        print(f"LR's coefficient of determination about testset : {test_score}")


MENUS = ["종료",  # 0
         "변환기(Transformer)를 적용한 데이터 확인하기",  # 1
         "다중 회귀 테스트",  # 2
         "특성을 추가했을 때 다중 회귀 테스트",  # 3
         ]

menu_options = {"1": lambda x: x.print_transformer_data(),
                "2": lambda x: x.lr_test(),
                "3": lambda x: x.lr_test_adding_feature(),
                }


if __name__ == '__main__':
    kr = MultipleReression()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
