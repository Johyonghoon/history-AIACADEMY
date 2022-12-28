import os
import keras.datasets.fashion_mnist
import numpy as np
from matplotlib import pyplot as plt
from keras.saving.save import load_model

from api.path import mnist


class MnistService:
    def __init__(self):
        global class_names
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def service_model(self, test_num) -> []:
        model = load_model(f"{mnist}\\save\\mnist_model.h5")
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        predictions = model.predict(test_images)
        i = test_num
        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        predicted_label = np.argmax(predictions_array)
        print(f"예측한 답 : {predicted_label}")
        result = f"'{predicted_label}'"
        return result


MNIST_MENUS = ["종료",  # 0
               "Mnist_Service",  # 1
               ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = MnistService()
    while True:
        menu = my_menu(MNIST_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.service_model())(t)
