import pandas as pd

import titanic
from util.dataset import Dataset
from util.menu import Menu


class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b =self.new_model(self.dataset.fname)
        return f'Train type: {type(b)}\n' \
               f'Train columns: {b.columns}\n' \
               f'Train head: {b.head()}\n' \
               f'Train null 개수: {b.isnull().sum()}'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        print(f'데이터프레임 내부 보기: \n{df}')
        return df

    @staticmethod
    def create_train(this) -> object:
        pass

    def create_label(self):
        pass

