from io import BytesIO

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from canny.models import LennaModel, image_read, gray_scale, ImageToNumberArray
from util.dataset import Dataset
import cv2 as cv
LENNA = "Lenna.png"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"


class LennaController(object):

    dataset = Dataset()
    model = LennaModel()

    def __init__(self):
        pass

    def __str__(self):
        return f''

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = image_read(params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f'Shape is {img.shape}')
        cv.imshow('Gray', img)
        cv.waitKey(0)
        cv.destroyAllwindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(arr)
        plt.imshow((lambda x: Image.fromarray(x))(img))
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        ### 디스크에서 읽는 경우 ###
        # img = cv.imread('./data/messi5.jpg', 0)
        ### 메모리에서 읽는 경우 BEGIN ###
        # url = "https://docs.opencv.org/4.x/roi.jpg"
        img = ImageToNumberArray(params[1])
        print(f'img typ : {type(img)}')
        edges = cv.Canny(img, 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 1, np.pi/180., 120, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    def submit(self):
        pass

