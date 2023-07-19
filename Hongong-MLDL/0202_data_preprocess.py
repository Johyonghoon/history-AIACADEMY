import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from utils import my_menu

warnings.simplefilter(action='ignore', category=FutureWarning)

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
               31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
               35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
               500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
               700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
               7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


class DataPreprocess:

    def __init__(self):
        global fish_data, fish_target, train_input, test_input, train_target, test_target
        fish_data = np.column_stack((fish_length, fish_weight))
        fish_target = np.concatenate((np.ones(35), np.zeros(14)))
        train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

    def og_knn_model(self):
        kn = KNeighborsClassifier()
        kn.fit(train_input, train_target)
        return kn

    def test_strange_fish(self):
        kn = self.og_knn_model()
        score = kn.score(test_input, test_target)
        print(f"KNN score : {score}")
        print(f"Test breem data(25, 150) : {kn.predict([[25, 150]])}")

        plt.scatter(train_input[:,0], train_input[:,1])
        plt.scatter(25, 150, marker='^')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def check_nearby_data(self):
        kn = self.og_knn_model()
        distances, indexes = kn.kneighbors([[25, 150]])

        plt.scatter(train_input[:,0], train_input[:,1])
        plt.scatter(25, 150, marker='^')
        plt.scatter(train_input[indexes, 0], train_input[indexes, 1], marker='D')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def check_scale(self):
        kn = self.og_knn_model()
        distances, indexes = kn.kneighbors([[25, 150]])

        plt.scatter(train_input[:,0], train_input[:,1])
        plt.scatter(25, 150, marker='^')
        plt.scatter(train_input[indexes, 0], train_input[indexes, 1], marker='D')
        plt.xlim((0, 1000))
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def apply_standard_score(self):
        mean = np.mean(train_input, axis=0)
        std = np.std(train_input, axis=0)
        print(f"평균 : {mean} / 표준편차 : {std}")
        train_scaled = (train_input - mean) / std
        return mean, std, train_scaled

    def check_standard_score(self):
        mean, std, train_scaled = self.apply_standard_score()
        new = ([25, 150] - mean) / std
        plt.scatter(train_scaled[:,0], train_scaled[:,1])
        plt.scatter(new[0], new[1], marker='^')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def algorithm(self):
        kn = KNeighborsClassifier()
        mean, std, train_scaled = self.apply_standard_score()
        kn.fit(train_scaled, train_target)
        test_scaled = (test_input - mean) / std
        score = kn.score(test_scaled, test_target)
        print(f"Score of trained model after data preprocess : {score}")
        new = ([25, 150] - mean) / std
        print(f"Predict data(25, 150) : {kn.predict([new])}")

        distances, indexes = kn.kneighbors([new])
        plt.scatter(train_scaled[:,0], train_scaled[:,1])
        plt.scatter(new[0], new[1], marker='^')
        plt.scatter(train_scaled[indexes, 0], train_scaled[indexes, 1], marker='D')
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()


MENUS = ["종료",  # 0
         "길이 25cm, 무게 150g 도미 예측하기",  # 1
         "가까운 데이터 확인하기",  # 2
         "스케일 확인하기",  # 3
         "표준점수로 변환한 데이터셋 확인하기",  # 4
         "데이터 전처리 후 테스트하기",  # 5
         ]

menu_options = {"1": lambda x: x.test_strange_fish(),
                "2": lambda x: x.check_nearby_data(),
                "3": lambda x: x.check_scale(),
                "4": lambda x: x.check_standard_score(),
                "5": lambda x: x.algorithm(),
                }


if __name__ == '__main__':
    knn = DataPreprocess()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](knn)
