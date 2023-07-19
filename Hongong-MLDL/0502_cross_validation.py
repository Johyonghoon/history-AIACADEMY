import numpy as np
import pandas as pd
from scipy.stats import uniform, randint
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier

from utils import my_menu


class CrossValidation:

    def __init__(self):
        global wine, sub_input, val_input, sub_target, val_target, train_input, test_input, train_target, test_target
        wine = pd.read_csv('https://bit.ly/wine_csv_data')
        data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
        target = wine['class'].to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(data, target,
                                                                              test_size=0.2, random_state=42)
        sub_input, val_input, sub_target, val_target = train_test_split(train_input, train_target,
                                                                        test_size=0.2, random_state=42)

    def decision_tree_with_validataion_data(self):
        dt = DecisionTreeClassifier(random_state=42)
        dt.fit(sub_input, sub_target)
        train_score = dt.score(sub_input, sub_target)
        val_score = dt.score(val_input, val_target)
        print(f"train score of Decision Tree Classifier : {train_score}")
        print(f"val score of Decision Tree Classifier : {val_score}")

    def decision_tree_with_cross_validation(self):
        dt = DecisionTreeClassifier(random_state=42)
        dt.fit(sub_input, sub_target)
        scores = cross_validate(dt, train_input, train_target)
        print(f"Cross Validation Function : \n {scores}")
        print(f"Final score of cross validate : {np.mean(scores['test_score'])}")

        # Mix train set
        splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
        scores = cross_validate(dt, train_input, train_target, cv=splitter)
        print(f"Final score of cross validate with mixed trainset : {np.mean(scores['test_score'])}")

    def grid_search(self):
        params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
        gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
        gs.fit(train_input, train_target)
        dt = gs.best_estimator_
        train_score = dt.score(train_input, train_target)
        print(f"train score of decision tree with grid search : {train_score}")
        print(f"Best Params : {gs.best_params_}")
        print(f"average score of cross validation : {gs.cv_results_['mean_test_score']}")
        best_index = np.argmax(gs.cv_results_['mean_test_score'])
        print(f"Find best parameter : {gs.cv_results_['params'][best_index]}")

    def find_best_params(self):
        params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
                  'max_depth': range(5, 20, 1),
                  'min_samples_split': range(2, 100, 10)
                  }
        gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
        gs.fit(train_input, train_target)
        print(f"Best params : {gs.best_params_}")
        print(f"Best score of cross validation : {np.max(gs.cv_results_['mean_test_score'])}")

    def random_search(self):
        params = {'min_impurity_decrease': uniform(0.0001, 0.001),
                  'max_depth': randint(20, 50),
                  'min_samples_split': randint(2, 25),
                  'min_samples_leaf': randint(1, 25),
                  }
        gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params, n_iter=100, n_jobs=-1, random_state=42)
        gs.fit(train_input, train_target)
        print(f"Best Params of Random Search : {gs.best_params_}")
        print(f"Best score of cross validation : {np.max(gs.cv_results_['mean_test_score'])}")

        dt = gs.best_estimator_
        test_score = dt.score(test_input, test_target)
        print(f"Final test with best params : {test_score}")


MENUS = ["종료",  # 0
         "검증 세트를 이용한 결정 트리",  # 1
         "교차 검증을 이용한 결정 트리",  # 2
         "그리드 서치",  # 3
         "최상의 파라미터 찾기",  # 4
         "랜덤 서치",  # 5
         ]

menu_options = {"1": lambda x: x.decision_tree_with_validataion_data(),
                "2": lambda x: x.decision_tree_with_cross_validation(),
                "3": lambda x: x.grid_search(),
                "4": lambda x: x.find_best_params(),
                "5": lambda x: x.random_search(),
                }

if __name__ == '__main__':
    kr = CrossValidation()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
