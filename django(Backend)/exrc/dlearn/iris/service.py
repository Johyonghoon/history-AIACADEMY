import os

import numpy as np
from sklearn import datasets
from keras.saving.save import load_model

from api.path import dir_path


class IrisService(object):
    def __init__(self):
        global model, target_names
        model = load_model(os.path.join(dir_path("iris"), "save", "iris_model.h5"))
        target_names = datasets.load_iris().target_names

    def service_model(self, features):
        features = np.reshape(features, (1, 4))
        Y_prob = model.predict(features, verbose=0)
        predicted = Y_prob.argmax(axis=-1)
        return predicted[0]  # p-value 가장 높은 것


IRIS_MENUS = ["종료",  # 0
              "IRIS",  # 1
              ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = IrisService()
    while True:
        menu = my_menu(IRIS_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.service_model())(t)
