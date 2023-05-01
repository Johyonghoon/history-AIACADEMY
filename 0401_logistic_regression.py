import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.special import expit, softmax
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from utils import my_menu

warnings.simplefilter(action='ignore', category=FutureWarning)


class LRModel:

    def __init__(self):
        global fish, fish_input, fish_target, train_input, test_input, train_target, test_target, \
            train_scaled, test_scaled
        fish = pd.read_csv('https://bit.ly/fish_csv_data')
        fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
        fish_target = fish['Species'].to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)
        train_scaled, test_scaled = self.transformer()

    def check_data(self):
        print(f"##### 상위 5개 행 출력하기 ##### \n"
              f"{fish.head()} \n\n"
              f"##### 생선 종류 확인하기(특정 컬럼 확인하기) ##### \n"
              f"{pd.unique(fish['Species'])} \n\n"
              f"##### 생선 종류를 타깃값으로 설정하고 다른 입력값을 특성으로 사용, 상위 5개 행 출력하기 ##### \n"
              f"{fish_input[:5]} \n\n" 
              f"##### 타깃값(생선 종류) 출력하기 ##### \n"
              f"{fish_target[:5]} \n")

    def transformer(self):
        ss = StandardScaler()
        ss.fit(train_input)
        train_scaled = ss.transform(train_input)
        test_scaled = ss.transform(test_input)
        return train_scaled, test_scaled

    def k_neighbors_classifier(self):
        kn = KNeighborsClassifier(n_neighbors=3)
        kn.fit(train_scaled, train_target)
        train_score = kn.score(train_scaled, train_target)
        test_score = kn.score(test_scaled, test_target)
        print(f"train score of KNeighborsClassifier : {train_score}")
        print(f"test score of KNeighborsClassifier : {test_score}")

        proba = kn.predict_proba(test_scaled[:5])
        print(np.round(proba, decimals=4))

        distances, indexes = kn.kneighbors(test_scaled[3:4])
        print(train_target[indexes])

    def graph_of_sigmoid(self):
        z = np.arange(-5, 5, 0.1)
        phi = 1 / (1 + np.exp(-z))
        plt.plot(z, phi)
        plt.xlabel('z')
        plt.ylabel('phi')
        plt.show()

    def lr_binary_classification(self):
        bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
        train_bream_smelt = train_scaled[bream_smelt_indexes]
        target_bream_smelt = train_target[bream_smelt_indexes]

        lr = LogisticRegression()
        lr.fit(train_bream_smelt, target_bream_smelt)
        print(f"Predict of 5 samples by : {lr.predict(train_bream_smelt[:5])}")
        print(f"classes : {lr.classes_}")
        print(f"coefficient and intercept of lr : {lr.coef_} / {lr.intercept_}")
        decisions = lr.decision_function(train_bream_smelt[:5])
        print(f"z score : {decisions}")
        print(f"probability : {expit(decisions)}")

    def lr_multiple_classification(self):
        lr = LogisticRegression(C=20, max_iter=1000)
        lr.fit(train_scaled, train_target)
        train_score = lr.score(train_scaled, train_target)
        test_score = lr.score(test_scaled, test_target)
        print(f"train score of lr multiple classification : {train_score}")
        print(f"test score of lr multiple classification : {test_score}")
        print(f"Predict of 5 samples : {lr.predict(test_scaled[:5])}")
        proba = lr.predict_proba(test_scaled[:5])
        print(f"Predicted probability : \n {np.round(proba, decimals=3)}")
        print(f"Classes : {lr.classes_}")
        print(f"Shape of coefficient and intercept : {lr.coef_.shape} / {lr.intercept_.shape}")

        decision = lr.decision_function(test_scaled[:5])
        print(f"Probability of decision funtion : {np.round(decision, decimals=2)}")

        proba = softmax(decision, axis=1)
        print(f"Probability of softmax function : {np.round(proba, decimals=3)}")


MENUS = ["종료",  # 0
         "데이터 확인하기",  # 1
         "k-최근접 이웃 분류기 확률 예측",  # 2
         "시그모이드 함수 그래프 확인",  # 3
         "로지스틱 회귀 이진 분류하기",  # 4
         "로지스틱 회귀 다중 분류하기",  # 5
         ]

menu_options = {"1": lambda x: x.check_data(),
                "2": lambda x: x.k_neighbors_classifier(),
                "3": lambda x: x.graph_of_sigmoid(),
                "4": lambda x: x.lr_binary_classification(),
                "5": lambda x: x.lr_multiple_classification(),
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
