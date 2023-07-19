import warnings
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

from utils import my_menu

warnings.simplefilter(action='ignore', category=FutureWarning)

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


class KNN:

    def __init__(self):
        global fish_data, fish_target
        length = bream_length + smelt_length
        weight = bream_weight + smelt_weight
        fish_data = [[l, w] for l, w in zip(length, weight)]
        fish_target = [1] * 35 + [0] * 14

    def bream_scatter_plot(self):
        plt.scatter(bream_length, bream_weight)
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def fishes_scatter_plot(self):
        plt.scatter(bream_length, bream_weight)
        plt.scatter(smelt_length, smelt_weight)
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def algorithm(self):
        kn = KNeighborsClassifier()
        kn.fit(fish_data, fish_target)
        score = kn.score(fish_data, fish_target)
        print(f"Result of that n_neighbors option is default : {score}")
        predict = kn.predict([[30, 600]])
        print(f"Predict(30, 600) : {predict}")

    def algorithm_n_neighbors_option_49(self):
        kn49 = KNeighborsClassifier(n_neighbors=49)  # n_neighbors default is 5
        kn49.fit(fish_data, fish_target)
        kn49_score = kn49.score(fish_data, fish_target)
        print(f"Result of that n_neighbors option is 49 : {kn49_score}")
        print(f"It's same with 35/49 = {35/49}")

    def find_not_hunnit_score(self):
        kn = KNeighborsClassifier()
        kn.fit(fish_data, fish_target)
        for n in range(5, 50):
            kn.n_neighbors = n
            score = kn.score(fish_data, fish_target)
            if score < 1:
                print(f"Not first hunnit score is {n} : {score} ")
                break


MENUS = ["종료",  # 0
         "도미 산점도 보기",  # 1
         "전체 생선 산점도 보기",  # 2
         "KNN 알고리즘 테스트",  # 3
         "KNN 알고리즘 옵션 n_neighbors 값이 49일 때",  # 4
         "KNN 알고리즘 테스트 점수가 100%가 아닌 n_neighbors 값 찾기",  # 5
         ]

menu_options = {"1": lambda x: x.bream_scatter_plot(),
                "2": lambda x: x.fishes_scatter_plot(),
                "3": lambda x: x.algorithm(),
                "4": lambda x: x.algorithm_n_neighbors_option_49(),
                "5": lambda x: x.find_not_hunnit_score(),
                }


if __name__ == '__main__':
    knn = KNN()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](knn)
