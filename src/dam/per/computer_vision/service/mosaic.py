from io import BytesIO
from PIL import Image
from matplotlib import pyplot as plt
from src.cmm.const.crawler import HEADERS
from src.cmm.service.menu import Menu
from src.utl.lambdas import MosaicLambda
import cv2 as cv
import numpy as np
import requests

MOSAIC_MENUS = ["종료",  # 0
                "원본보기",  # 1
                "그레이스케일",  # 2
                "엣지검출",  # 3
                "직선검출",  # 4
                "모자이크",  # 5
                "소녀 모자이크",  # 6
                "모녀 모자이크"  # 7
                ]

LENNA = "./../../../../../static/data/dam/per/computer_vision/mosaic/Lenna.png"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING="http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
CAT = "./../../../../../static/data/dam/per/computer_vision/mosaic/cat.jpg"
CAT_MOSAIC = "./../../../../../static/save/dam/per/computer_vision/mosaic/cat_mosaic.jpg"
GIRL = "./../../../../../static/data/dam/per/computer_vision/mosaic/girl.jpg"
HAAR = "./../../../../../static/data/dam/per/computer_vision/mosaic/haarcascade_frontalface_alt.xml" # 가중치 파일
PEOPLE = "./../../../../../static/data/dam/per/computer_vision/mosaic/people.jpg"


def ImageToNumberArray(url):
    res = requests.get(url, headers=HEADERS)
    image = Image.open(BytesIO(res.content))
    return np.array(image)


def Hough(edges):
    lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
    dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
    return dst


def Haar(*params):
    img_original = params[0]
    haar = params[1]
    face = haar.detectMultiScale(img_original, minSize=(150, 150))
    if len(face) == 0:
        print(f"얼굴인식 실패")
        quit()
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
    x1, y1, x2, y2 = x, y, x+w, y+h

    return x1, y1, x2, y2


def Canny(img):
    return cv.Canny(np.array(img), 10, 100)


def Haar_context(haar):
    return cv.CascadeClassifier(f"{haar}")


def Mosaic(img, rect, size):
    (x1, y1, x2, y2) = rect  # HAAR로 출력된 사각형 박스의 좌표값
    w = x2 - x1  # 좌표의 차가 rect의 길이
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    i_small = cv.resize(i_rect, (size, size))
    i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


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
        # static = GaussianBlur(static, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # static = Canny(static, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
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
        edges = cv.Canny(np.array(building_original), 10, 100) # (image, threshold 1=100, threshold 2=200)
        building_hough = Hough(edges)
        plt.subplot(122), plt.imshow(building_hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def menu_5_mosaic(*params):
        print(params[0])
        cat = cv.imread(f'{params[1]}')
        mos = Mosaic(cat, (150, 150, 450, 450), 10)
        cv.imwrite(CAT_MOSAIC, mos)
        cv.imshow(CAT_MOSAIC, mos)
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


if __name__ == '__main__':
    api = MosaicController()
    while True:
        menu = Menu.menu(MOSAIC_MENUS)
        if menu == "0":
            api.menu_0(MOSAIC_MENUS[0])
            break
        elif menu == "1": api.menu_1_original(MOSAIC_MENUS[1], LENNA)
        elif menu == "2": api.menu_2_grayscale(MOSAIC_MENUS[2], SOCCER)
        elif menu == "3": api.menu_3_canny(MOSAIC_MENUS[3], SOCCER)
        elif menu == "4": api.menu_4_hough(MOSAIC_MENUS[4], BUILDING)
        elif menu == "5": api.menu_5_mosaic(MOSAIC_MENUS[5], CAT)
        elif menu == "6": api.menu_6_girl_mosaic(MOSAIC_MENUS[6], HAAR, GIRL)
        elif menu == "7": api.menu_7_mosaics(MOSAIC_MENUS[7], HAAR, PEOPLE)
        else:
            print(" ### 해당 메뉴 없음 ### ")






