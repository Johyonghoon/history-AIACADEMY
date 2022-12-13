from keras import datasets
from keras.saving.save import load_model
import tensorflow as tf


class IrisService(object):
    def __init__(self):
        model = load_model('./save/iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_names

    def iris_hook(self):
        self.service_model()

    def service_model(self):
        pass





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
            (lambda x: x.iris_hook())(t)
