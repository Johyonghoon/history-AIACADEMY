import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

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
        global train_input, test_input, train_target, test_target, train_scaled, test_scaled
        df = pd.read_csv('https://bit.ly/perch_csv_data')
        perch_full = df.to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)
        train_scaled, test_scaled = self.standard_scaler()

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

    def standard_scaler(self):
        ss = StandardScaler()
        poly, train_poly, test_poly = self.transformer()
        ss.fit(train_poly)
        train_scaled = ss.transform(train_poly)
        test_scaled = ss.transform(test_poly)
        return train_scaled, test_scaled

    def ridge_regression(self):
        ridge = Ridge()
        ridge.fit(train_scaled, train_target)
        train_score = ridge.score(train_scaled, train_target)
        test_score = ridge.score(test_scaled, test_target)
        print(f"train score of ridge regression : {train_score}")
        print(f"test score of ridge regression : {test_score}")

    def graph_of_rr_score(self):
        train_score = []
        test_score = []
        alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
        for alpha in alpha_list:
            ridge = Ridge(alpha=alpha)
            ridge.fit(train_scaled, train_target)
            train_score.append(ridge.score(train_scaled, train_target))
            test_score.append(ridge.score(test_scaled, test_target))

        plt.plot(np.log10(alpha_list), train_score)
        plt.plot(np.log10(alpha_list), test_score)
        plt.xlabel('alpha')
        plt.ylabel('R^2')
        plt.show()

    def optimal_ridge_regression(self):
        ridge = Ridge(alpha=0.1)
        ridge.fit(train_scaled, train_target)
        train_score = ridge.score(train_scaled, train_target)
        test_score = ridge.score(test_scaled, test_target)
        print(f"train score of optimal ridge regression : {train_score}")
        print(f"test score of optimal ridge regression : {test_score}")

    def lasso_regression(self):
        lasso = Lasso()
        lasso.fit(train_scaled, train_target)
        train_score = lasso.score(train_scaled, train_target)
        test_score = lasso.score(test_scaled, test_target)
        print(f"train score of lasso regression : {train_score}")
        print(f"test score of lasso regression : {test_score}")

    def graph_of_lr_score(self):
        train_score = []
        test_score = []
        alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
        for alpha in alpha_list:
            lasso = Lasso(alpha=alpha, max_iter=10000)
            lasso.fit(train_scaled, train_target)
            train_score.append(lasso.score(train_scaled, train_target))
            test_score.append(lasso.score(test_scaled, test_target))

        plt.plot(np.log10(alpha_list), train_score)
        plt.plot(np.log10(alpha_list), test_score)
        plt.xlabel('alpha')
        plt.ylabel('R^2')
        plt.show()

    def optimal_lasso_regression(self):
        lasso = Lasso(alpha=10)
        lasso.fit(train_scaled, train_target)
        train_score = lasso.score(train_scaled, train_target)
        test_score = lasso.score(test_scaled, test_target)
        print(f"train score of optimal lasso regression : {train_score}")
        print(f"test score of optimal lasso regression : {test_score}")


MENUS = ["종료",  # 0
         "변환기(Transformer)를 적용한 데이터 확인하기",  # 1
         "다중 회귀 테스트",  # 2
         "특성을 추가했을 때 다중 회귀 테스트",  # 3
         "릿지 회귀",  # 4
         "릿지 회귀의 적합한 alpha 값 찾기",  # 5
         "최적의 alpha 값을 적용한 릿지 회귀",  # 6
         "라쏘 회귀",  # 7
         "라쏘 회귀의 적합한 alpha 값 찾기",  # 8
         "최적의 alpha 값을 적용한 라쏘 회귀",  # 9
         ]

menu_options = {"1": lambda x: x.print_transformer_data(),
                "2": lambda x: x.lr_test(),
                "3": lambda x: x.lr_test_adding_feature(),
                "4": lambda x: x.ridge_regression(),
                "5": lambda x: x.graph_of_rr_score(),
                "6": lambda x: x.optimal_ridge_regression(),
                "7": lambda x: x.lasso_regression(),
                "8": lambda x: x.graph_of_lr_score(),
                "9": lambda x: x.optimal_lasso_regression(),
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
