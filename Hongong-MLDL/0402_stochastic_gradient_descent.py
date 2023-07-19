import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from utils import my_menu

warnings.simplefilter(action='ignore', category=FutureWarning)


class SGDModel:

    def __init__(self):
        global fish_input, fish_target, train_input, test_input, train_target, test_target, train_scaled, test_scaled
        fish = pd.read_csv('https://bit.ly/fish_csv_data')
        fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
        fish_target = fish['Species'].to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)
        train_scaled, test_scaled = self.transformer()

    def transformer(self):
        ss = StandardScaler()
        ss.fit(train_input)
        train_scaled = ss.transform(train_input)
        test_scaled = ss.transform(test_input)
        return train_scaled, test_scaled

    def stochastic_gradient_descent(self):
        sc = SGDClassifier(loss='log', max_iter=10, random_state=42)
        sc.fit(train_scaled, train_target)
        train_score = sc.score(train_scaled, train_target)
        test_score = sc.score(test_scaled, test_target)
        print(f"train score of SGDClassifier : {train_score}")
        print(f"test score of SGDClassifier : {test_score}")

        sc.partial_fit(train_scaled, train_target)
        train_score = sc.score(train_scaled, train_target)
        test_score = sc.score(test_scaled, test_target)
        print(f"train score of SGDClassifier with partial fit : {train_score}")
        print(f"test score of SGDClassifier with partial fit : {test_score}")

    def early_stopping(self):
        sc = SGDClassifier(loss='log', random_state=42)
        train_score = []
        test_score = []
        classes = np.unique(train_target)
        for _ in range(0, 300):
            sc.partial_fit(train_scaled, train_target, classes=classes)
            train_score.append(sc.score(train_scaled, train_target))
            test_score.append(sc.score(test_scaled, test_target))

        plt.plot(train_score)
        plt.plot(test_score)
        plt.xlabel('epoch')
        plt.ylabel('accuracy')
        plt.show()

    def optimal_sgdc(self):
        sc = SGDClassifier(loss='log', max_iter=100, tol=None, random_state=42)
        sc.fit(train_scaled, train_target)
        train_score = sc.score(train_scaled, train_target)
        test_score = sc.score(test_scaled, test_target)
        print(f"train score of optimal SGDClassifier : {train_score}")
        print(f"test score of optimal SGDClassifier : {test_score}")

    def hinge_of_loss_parameter_of_sgdc(self):
        sc = SGDClassifier(loss='hinge', max_iter=100, tol=None, random_state=42)  # loss parameter's default is hinge
        sc.fit(train_scaled, train_target)
        train_score = sc.score(train_scaled, train_target)
        test_score = sc.score(test_scaled, test_target)
        print(f"train score of SGDClassifier with hinge loss parameter : {train_score}")
        print(f"test score of SGDClassifier with hinge loss parameter : {test_score}")


MENUS = ["종료",  # 0
         "SGDClassifier",  # 1
         "조기 종료 확인하기",  # 2
         "적합한 epoche를 적용한 SGDClassifier 결과값 확인하기",  # 3
         "[참고] hinge 손실함수를 적용한 SGDClassifier 결과값 확인하기",  # 4
         ]

menu_options = {"1": lambda x: x.stochastic_gradient_descent(),
                "2": lambda x: x.early_stopping(),
                "3": lambda x: x.optimal_sgdc(),
                "4": lambda x: x.hinge_of_loss_parameter_of_sgdc(),
                }


if __name__ == '__main__':
    kr = SGDModel()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
            