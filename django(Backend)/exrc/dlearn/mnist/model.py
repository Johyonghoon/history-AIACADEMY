import os

import tensorflow as tf

from api.path import dir_path


class MnistModel:
    def __init__(self):
        global mnist_set, x_train, y_train, x_test, y_test
        mnist_set = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

    def create_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])
        # print(f" --- feature name --- \n{model.summary()}")
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=5)
        test_loss, test_acc = model.evaluate(x_test, y_test)
        print('테스트 정확도:', test_acc)

        file_name = os.path.join(dir_path("mnist"), "save", "mnist_model.h5")
        model.save(file_name)


MNIST_MENUS = ["종료",  # 0
               "MNIST",  # 1
               ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = MnistModel()
    while True:
        menu = my_menu(MNIST_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.create_model())(t)
