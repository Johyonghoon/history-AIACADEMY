import warnings
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, HistGradientBoostingClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split, cross_validate
# from sklearn.experimental import enable_hist_gradient_boosting
from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier  # do not work at python3.8

from utils import my_menu

warnings.simplefilter(action='ignore', category=FutureWarning)


class EnsembleOfTree:

    def __init__(self):
        global wine, train_input, test_input, train_target, test_target
        wine = pd.read_csv('https://bit.ly/wine_csv_data')
        data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
        target = wine['class'].to_numpy()
        train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

    def random_forest(self):
        rf = RandomForestClassifier(n_jobs=-1, random_state=42)
        scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
        print(f"Train score / Test score : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")

        rf.fit(train_input, train_target)
        print(f"Feature Importances : {rf.feature_importances_}")

    def random_forest_with_oob_samples(self):
        rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
        rf.fit(train_input, train_target)
        print(f"OOB Score : {rf.oob_score_}")

    def extra_trees(self):
        et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
        scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=-1)
        print(f"Train score / Test score of extra trees : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")

        et.fit(train_input, train_target)
        print(f"Feature Importances : {et.feature_importances_}")

    def gradient_boosting(self):
        gb = GradientBoostingClassifier(random_state=42)
        scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
        print(f"Train score / Test score of gradient boosting : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")

        print(f"---------------------------------------------------------------------------------------------- \n"
              f"----------------------------- Increasing the Decision Tree by 5x -----------------------------")

        gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
        scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
        print(f"Train score / Test score of gradient boosting(x5) : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")
        gb.fit(train_input, train_target)
        print(f"Feature Importances : {gb.feature_importances_}")

    def histogram_based_gradient_boosting(self):
        hgb = HistGradientBoostingClassifier(random_state=42)
        scores = cross_validate(hgb, train_input, train_target, return_train_score=True)
        print(f"Train score / Test score : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")

        hgb.fit(train_input, train_target)
        result = permutation_importance(hgb, train_input, train_target, n_repeats=10, random_state=42, n_jobs=-1)
        print(f"Train Feature Importances mean : {result.importances_mean}")

        result = permutation_importance(hgb, test_input, test_target, n_repeats=10, random_state=42, n_jobs=-1)
        print(f"Test Feature Importances mean : {result.importances_mean}")
        print(f"Test Score : {hgb.score(test_input, test_target)}")

    def xgboost(self):
        xgb = XGBClassifier(tree_method='hist', random_state=42)
        scores = cross_validate(xgb, train_input, train_target, return_train_score=True)
        print(f"Train score / Test score : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")

    # do not work at python3.8
    # def lightgbm_of_ms(self):
    #     lgb = LGBMClassifier(random_state=42)
    #     scores = cross_validate(lgb, train_input, train_target, return_train_score=True, n_jobs=-1)
    #     print(f"Train score / Test score : {np.mean(scores['train_score'])} / {np.mean(scores['test_score'])}")


MENUS = ["종료",  # 0
         "랜덤 포레스트 분류",  # 1
         "OOB 샘플을 통해 평가한 랜덤 포레스트 점수 출력",  # 2
         "엑스트라 트리",  # 3
         "그레이디언트 부스팅",  # 4
         "히스토그램 그레이디언트 부스팅",  # 5
         "XGBoost",  # 6
         # "LightGBM",  # 7
         ]

menu_options = {"1": lambda x: x.random_forest(),
                "2": lambda x: x.random_forest_with_oob_samples(),
                "3": lambda x: x.extra_trees(),
                "4": lambda x: x.gradient_boosting(),
                "5": lambda x: x.histogram_based_gradient_boosting(),
                "6": lambda x: x.xgboost(),
                # "7": lambda x: x.lightgbm_of_ms(),
                }

if __name__ == '__main__':
    kr = EnsembleOfTree()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            menu_options[menu](kr)
