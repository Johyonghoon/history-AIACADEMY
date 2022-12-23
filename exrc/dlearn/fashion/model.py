import os.path

import keras.datasets.fashion_mnist
from keras import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt


class FashionModel(object):

    def create_model(self):
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        plt.figure()
        plt.imshow(train_images[10])
        plt.colorbar()
        plt.grid(False)
        plt.show()

        model = Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print(f"Test Accuracy is {test_acc}")
        file_name = r"C:\Users\AIA\PycharmProjects\djangoProject\exrc\dlearn\fashion\save\fashion_model.h5"
        model.save(file_name)


FASHION_MENUS = ["종료",  # 0
                 "Fashion",  # 1
                 ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = FashionModel()
    while True:
        menu = my_menu(FASHION_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.create_model())(t)
