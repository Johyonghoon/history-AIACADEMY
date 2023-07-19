import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

from utils import my_menu


class DecisionTree:

    def __init__(self):
        global wine, train_input, test_input, train_target, test_target, train_scaled, test_scaled
        wine = pd.read_csv('https://bit.ly/wine_csv_data')
        data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
        target = wine['class'].to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)
        train_scaled, test_scaled = self.transformer()

    def print_wine_data(self):
        print(f"##### 와인 데이터 상위 5개 출력하기 ##### \n"
              f"{wine.head()} \n\n"  # Red wine : 0 / White wine : 1
              f"##### 데이터프레임 각 열의 데이터 타입과 누락된 데이터 확인 ##### \n"
              f"{wine.info()} \n\n "
              f"##### 열에 대한 간략한 통계 출력 ##### \n"
              f"{wine.describe()} \n")
        print(f"shape of trainset and testset : {train_input.shape} / {test_input.shape}")

    def transformer(self):
        ss = StandardScaler()
        ss.fit(train_input)
        train_scaled = ss.transform(train_input)
        test_scaled = ss.transform(test_input)
        return train_scaled, test_scaled

    def logistic_regression(self):
        lr = LogisticRegression()
        lr.fit(train_scaled, train_target)
        train_score = lr.score(train_scaled, train_target)
        test_score = lr.score(test_scaled, test_target)
        print(f"train score of Logistic Regression : {train_score}")
        print(f"test score of Logistic Regression : {test_score}")

    def decision_tree(self):
        dt = DecisionTreeClassifier(random_state=42)
        dt.fit(train_scaled, train_target)
        train_score = dt.score(train_scaled, train_target)
        test_score = dt.score(test_scaled, test_target)
        print(f"train score of Decision Tree Classifier : {train_score}")
        print(f"test score of Decision Tree Classifier : {test_score}")

        plt.figure(figsize=(10, 7))
        plot_tree(dt)
        plt.show()

    def pruning(self):
        dt = DecisionTreeClassifier(max_depth=3, random_state=42)
        dt.fit(train_scaled, train_target)
        train_score = dt.score(train_scaled, train_target)
        test_score = dt.score(test_scaled, test_target)
        print(f"train score of Decision Tree Classifier with pruning : {train_score}")
        print(f"test score of Decision Tree Classifier with pruning : {test_score}")

        plt.figure(figsize=(20, 15))
        plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
        plt.show()

        print(f"Feagure Importances : {dt.feature_importances_}")

    def do_not_need_transformer(self):
        dt = DecisionTreeClassifier(max_depth=3, random_state=42)
        dt.fit(train_input, train_target)
        train_score = dt.score(train_input, train_target)
        test_score = dt.score(test_input, test_target)
        print(f"train score of Decision Tree Classifier with input data without preprocess : {train_score}")
        print(f"test score of Decision Tree Classifier with input data without preprocess : {test_score}")

        plt.figure(figsize=(20, 15))
        plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
        plt.show()


MENUS = ["종료",  # 0
         "와인 데이터 확인하기",  # 1
         "Logistic Regression",  # 2
         "Decision Tree Classifier",  # 3
         "결정 트리 가지치기",  # 4
         "[참고] 결정 트리는 전처리가 필요없다.",  # 5
         ]

menu_options = {"1": lambda x: x.print_wine_data(),
                "2": lambda x: x.logistic_regression(),
                "3": lambda x: x.decision_tree(),
                "4": lambda x: x.pruning(),
                "5": lambda x: x.do_not_need_transformer(),
                }

if __name__ == '__main__':
    kr = DecisionTree()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
