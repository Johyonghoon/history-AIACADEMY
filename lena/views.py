import cv2

from lena.models import LennaModels
from util.dataset import Dataset


class LennaController(object):

    dataset = Dataset()
    model = LennaModels()

    def __init__(self):
        pass

    def __str__(self):
        return f''

    def preprocess(self, fname) -> object:
        img = self.model.new_model(fname)
        return img

    def modeling(self, fname) -> object:
        img = self.preprocess(fname)
        return img

    def submit(self):
        pass

