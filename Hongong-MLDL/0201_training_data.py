import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

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


class TrainingData:

    def __init__(self):
        global fish_data, fish_target
        fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
        fish_target = [1] * 35 + [0] * 14

    def sampling_bias(self):
        kn = KNeighborsClassifier()
        train_input = fish_data[:35]
        train_target = fish_target[:35]
        test_input = fish_data[35:]
        test_target = fish_target[35:]
        kn.fit(train_input, train_target)
        score = kn.score(test_input, test_target)
        print(f"Result of sampling bias : {score}")

    def array_indexing(self):
        input_arr = np.array(fish_data)
        target_arr = np.array(fish_target)
        np.random.seed(42)
        index = np.arange(49)
        np.random.shuffle(index)

        self.train_input = input_arr[index[:35]]
        self.train_target = target_arr[index[:35]]
        self.test_input = input_arr[index[35:]]
        self.test_target = target_arr[index[35:]]

    def show_array_indexing(self):
        self.array_indexing()
        plt.scatter(self.train_input[:,0], self.train_input[:,1])
        plt.scatter(self.test_input[:,0], self.test_input[:,1])
        plt.xlabel('length')
        plt.ylabel('weight')
        plt.show()

    def algorithm(self):
        self.array_indexing()
        kn = KNeighborsClassifier()
        kn.fit(self.train_input, self.train_target)
        score = kn.score(self.test_input, self.test_target)
        print(f"Result of KNN algorithm : {score}")


MENUS = ["종료",  # 0
         "샘플링 편향 테스트",  # 1
         "배열 인덱싱 확인하기",  # 2
         "KNN 알고리즘 테스트",  # 3
         ]

menu_options = {"1": lambda x: x.sampling_bias(),
                "2": lambda x: x.show_array_indexing(),
                "3": lambda x: x.algorithm(),
                }


if __name__ == '__main__':
    knn = TrainingData()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](knn)
