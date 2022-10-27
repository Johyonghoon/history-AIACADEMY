import pandas as pd

from util.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        print(f'데이터프레임 내부 보기: \n{df}')
        return df

    def create_train(self):
        pass

    def create_label(self):
        pass