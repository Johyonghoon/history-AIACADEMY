import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

from utils import my_menu

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
                         21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
                         23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
                         27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
                         39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
                         44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
                         115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
                         150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
                         218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
                         556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
                         850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
                         1000.0])


class LRModel:

    def __init__(self):
        global train_input, test_input, train_target, test_target
        train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)
        train_input = train_input.reshape(-1, 1)
        test_input = test_input.reshape(-1, 1)

    def knr_model(self):
        knr = KNeighborsRegressor(n_neighbors=3)
        knr.fit(train_input, train_target)
        return knr

    def check_knr_scatter_plot(self):
        knr = self.knr_model()
        distances, indexes = knr.kneighbors([[50]])
        plt.scatter(train_input, train_target)
        plt.scatter(train_input[indexes], train_target[indexes], marker='D')
        plt.scatter(50, 1033, marker='^')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def lr_model(self, input, target):
        lr = LinearRegression()
        lr.fit(input, target)
        return lr

    def linear_regression(self):
        lr = self.lr_model(train_input, train_target)
        score = lr.predict([[50]])
        print(f"Predict 50cm perch's weight by linear regression : {score}")

        print(f"LinearRegression's coefficient and intercept : {lr.coef_}, {lr.intercept_}")
        train_score = lr.score(train_input, train_target)
        test_score = lr.score(test_input, test_target)
        print(f"LR's coefficient of determination about trainset : {train_score}")
        print(f"LR's coefficient of determination about testset : {test_score}")

    def polynomial_regression(self):
        self.train_poly = np.column_stack((train_input ** 2, train_input))
        self.test_poly = np.column_stack((test_input ** 2, test_input))

        lr = self.lr_model(self.train_poly, train_target)

        score = lr.predict([[50 ** 2, 50]])
        print(f"Predict 50cm perch's weight by polynomial regression : {score}")
        print(f"Polynomial Regression's coefficient and intercept : {lr.coef_}, {lr.intercept_}")

    def check_pr_scatter_plot(self):
        point = np.arange(15, 50)
        plt.scatter(train_input, train_target)
        plt.plot(point, 1.01 * point ** 2 - 21.6 * point + 116.05)
        plt.scatter(50, 1574, marker='^')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

        lr = self.lr_model(self.train_poly, train_target)
        train_score = lr.score(self.train_poly, train_target)
        test_score = lr.score(self.test_poly, test_target)
        print(f"LR's coefficient of determination about trainset : {train_score}")
        print(f"LR's coefficient of determination about testset : {test_score}")


MENUS = ["종료",  # 0
         "산점도 확인하기",  # 1
         "선형 회귀를 통해 50cm 농어 무게 예측하기",  # 2
         "다항 회귀를 통해 50cm 농어 무게 예측하기",  # 3
         "다항 회귀 방정식 그래프를 포함한 산점도 확인하기",  # 4
         ]

menu_options = {"1": lambda x: x.check_knr_scatter_plot(),
                "2": lambda x: x.linear_regression(),
                "3": lambda x: x.polynomial_regression(),
                "4": lambda x: x.check_pr_scatter_plot(),
                }


if __name__ == '__main__':
    kr = LRModel()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
