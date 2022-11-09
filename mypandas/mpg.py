import pandas as pd


MENUS = ['종료', 'mpg 앞부분 확인', 'mpg 뒷부분 확인', '행,열 출력', '데이터 속성 확인', '요약 통계량 출력', '문자 변수 요약 통계량 함께 출력']


def mpg_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i} : {j}")
    return input("메뉴 선택 : ")


class MpgController:

    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')

    def menu_1_mpg_head(self):
        print(self.mpg.head())

    def menu_2_mpg_tail(self):
        print(self.mpg.tail())

    def menu_3_mpg_shape(self):
        print(self.mpg.shape)

    def menu_4_mpg_info(self):
        print(self.mpg.info())

    def menu_5_mpg_describe(self):
        print(self.mpg.describe())

    def menu_6_mpg_describe_all(self):
        print(self.mpg.describe(include='all'))


if __name__ == '__main__':
    api = MpgController()
    while True:
        menu = mpg_menu(MENUS)
        if menu == '0':
            print(MENUS[0])
            break
        elif menu == '1':
            print(MENUS[1])
            api.menu_1_mpg_head()
        elif menu == '2':
            print(MENUS[2])
            api.menu_2_mpg_tail()
        elif menu == '3':
            print(MENUS[3])
            api.menu_3_mpg_shape()
        elif menu == '4':
            print(MENUS[4])
            api.menu_4_mpg_info()
        elif menu == '5':
            print(MENUS[5])
            api.menu_5_mpg_describe()
        elif menu == '6':
            print(MENUS[6])
            api.menu_6_mpg_describe_all()
        else:
            print("다시 입력하세요.")

