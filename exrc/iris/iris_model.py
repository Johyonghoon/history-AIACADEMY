import os

from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder


class IrisModel(object):
    def __init__(self):
        global iris, _X, _Y
        iris = datasets.load_iris()
        print(f'type {type(iris)}')  # type <class 'sklearn.utils._bunch.Bunch'>
        _X = iris.data
        _Y = iris.target

    def iris_hook(self):
        # self.spec()
        self.create_model()

    def spec(self):
        print(f" --- feature name --- \n{iris.feature_names}\n"
              f" --- target name --- \n{iris.target_names}\n"
              f" --- data info --- \n{iris.DESCR}")

    """
    Shape (150, 6)    
     --- feature name --- 
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    """

    def create_model(self):
        X = _X
        Y = _Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, Y_1hot, epochs=300, batch_size=10)
        print('Model Training is completed')

        file_name = os.path.join(os.path.abspath("save"), "iris_model.h5")
        model.save(file_name)
        print(f"Model Saved in {file_name}")





IRIS_MENUS = ["종료",  # 0
              "IRIS",  # 1
              ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':
    t = IrisModel()
    while True:
        menu = my_menu(IRIS_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            (lambda x: x.iris_hook())(t)
