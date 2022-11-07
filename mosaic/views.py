from matplotlib import pyplot as plt
from mosaic.services import ImageToNumberArray, Hough, Haar, Mosaic, Canny, Haar_context
from util.lambdas import MosaicLambda
import cv2 as cv
import numpy as np

from util.dataset import Dataset


class MosaicController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1_original(*params):
        print(params[0])
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2_grayscale(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        img = MosaicLambda('GRAY_SCALE', arr)
        plt.imshow(MosaicLambda('IMAGE_FROM_ARRAY', img))
        plt.show()


    @staticmethod
    def menu_3_canny(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        # img = GaussianBlur(img, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # img = Canny(img, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4_hough(*params):
        print(params[0])
        building_original = ImageToNumberArray(params[1])
        plt.subplot(121), plt.imshow(building_original, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        edges = Canny(building_original) # (image, threshold 1=100, threshold 2=200)
        building_hough = Hough(edges)
        plt.subplot(122), plt.imshow(building_hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def menu_5_mosaic(*params):
        print(params[0])
        cat = cv.imread(f'{Dataset().context}{params[1]}')
        mos = Mosaic(cat, (150, 150, 450, 450), 10)
        cv.imwrite(f'{Dataset().context}cat-mossaic.png', mos)
        cv.imshow('CAT MOSAIC', mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6_girl_mosaic(*param):
        print(param[0])
        girl_control = MosaicLambda('IMAGE_READ_FOR_PLT', param[2])
        girl_original = girl_control.copy()
        girl_gray = MosaicLambda('GRAY_SCALE', girl_control)
        girl_canny = Canny(girl_control)
        girl_hough = Hough(girl_canny)
        haar = param[1]
        haar = Haar_context(haar)
        x1, y1, x2, y2 = Haar(girl_control, haar)
        rect = (x1, y1, x2, y2)
        red = (255, 0, 0)
        girl_haar = cv.rectangle(girl_control, (x1, y1), (x2, y2), red, thickness=20)
        girl_mos = Mosaic(girl_original, rect, 10)

        plt.subplot(161), plt.imshow(girl_original, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(girl_haar, cmap='gray')
        plt.title('HAAR'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(girl_mos, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_7_mosaics(*param):
        print(param[0])
        haar = param[1]
        haar = Haar_context(haar)
        img_original = MosaicLambda('IMAGE_READ_FOR_PLT', param[2])
        img_control = img_original.copy()
        face = haar.detectMultiScale(img_control, minSize=(150, 150))
        while True:
            if len(face) == 0:
                print(f"얼굴인식 실패")
                quit()
            for (x, y, w, h) in face:
                print(f'얼굴의 좌표 : {x},{y},{w},{h}')
                rect = x, y, x+w, y+h
                Mosaic(img_control, rect, 10)

        plt.imshow(img_control, cmap='gray')
        plt.title('Mosaics'), plt.xticks([]), plt.yticks([])
        plt.show()
"""
        img_original = params[0]
        haar = params[1]
        face = haar.detectMultiScale(img_original, minSize=(150, 150))
        if len(face) == 0:
            print(f"얼굴인식 실패")
            quit()
        for (x, y, w, h) in face:
            print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        x1, y1, x2, y2 = x, y, x + w, y + h
"""
"""
        plt.imshow(girl_original, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()

"""








