import cv2
import pandas as pd

from util.dataset import Dataset


class LennaModels(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        return f''

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = './data/'
        img = cv2.imread(this.context + fname)
        return img



