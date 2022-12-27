import os
import keras.datasets.fashion_mnist
import numpy as np
from matplotlib import pyplot as plt
from keras.saving.save import load_model

from api.path import fashion


class FashionService(object):
    def __init__(self):
        global class_names
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def service_model(self, test_num) -> []:
        # os.path.join(os.path.abspath("save"), "fashion_model.h5")
        model = load_model(f"{fashion}\\save\\fashion_model.h5")
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        predictions = model.predict(test_images)
        i = test_num
        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        predicted_label = np.argmax(predictions_array)
        print(f"예측한 답 : {predicted_label}")
        result = predicted_label
        if result == 0:
            resp = 'T-shirt/top'
        elif result == 1:
            resp = 'Trouser'
        elif result == 2:
            resp = 'Pullover'
        elif result == 3:
            resp = 'Dress'
        elif result == 4:
            resp = 'Coat'
        elif result == 5:
            resp = 'Sandal'
        elif result == 6:
            resp = 'Shirt'
        elif result == 7:
            resp = 'Sneaker'
        elif result == 8:
            resp = 'Bag'
        elif result == 9:
            resp = 'Ankle boot'
        return resp


FASHION_MENUS = ["종료",  # 0
                 "Fashion_Service",  # 1
                 ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = FashionService()
    while True:
        menu = my_menu(FASHION_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.service_model())(t)
