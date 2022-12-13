from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder


class IrisModel(object):
    def __init__(self):
        self.iris = datasets.load_iris()
        self._X = self.iris.data
        self._Y = self.iris.target

    def iris_hook(self):
        self.spec()
        # self.create_model()

    def spec(self):
        print(f" --- feature name --- \n{self.iris.feature_names}")
    """
    Shape (150, 6)    
     --- feature name --- 
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    """

    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, Y_1hot, epochs=300, batch_size=10)
        print('Model Training is completed')

        file_name = './save/iris_model.h5'
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
