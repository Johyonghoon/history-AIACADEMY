import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

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


class KNRModel:

    def __init__(self):
        global train_input, test_input, train_target, test_target
        train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)
        train_input = train_input.reshape(-1, 1)
        test_input = test_input.reshape(-1, 1)

    def check_scatter_plot(self):
        plt.scatter(perch_length, perch_weight)
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def test_algorithm(self):
        knr = KNeighborsRegressor()
        knr.fit(train_input, train_target)
        test_score = knr.score(test_input, test_target)
        print(f"KNR's coefficient of determination about testset : {test_score}")

        test_prediction = knr.predict(test_input)
        mae = mean_absolute_error(test_target, test_prediction)
        print(f"KNR's mean_absolute_error : {mae}")

        train_score = knr.score(train_input, train_target)
        print(f"KNR's coefficient of determination about trainset : {train_score}")

    def fitting(self):
        knr = KNeighborsRegressor()
        knr.n_neighbors = 3
        knr.fit(train_input, train_target)

        test_score = knr.score(test_input, test_target)
        print(f"KNR's coefficient of determination about testset : {test_score}")
        train_score = knr.score(train_input, train_target)
        print(f"KNR's coefficient of determination about trainset : {train_score}")



MENUS = ["종료",  # 0
         "산점도 확인하기",  # 1
         "k-최근접 이웃 회귀 테스트",  # 2
         "k-최근접 이웃 회귀 피팅하기",  # 3
         ]

menu_options = {"1": lambda x: x.check_scatter_plot(),
                "2": lambda x: x.test_algorithm(),
                "3": lambda x: x.fitting(),
                }


if __name__ == '__main__':
    kr = KNRModel()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
