import string

import numpy as np
import pandas as pd


MENUS = ['종료', '과일2D', '숫자2D']


def fruit_menu(ls):
    [print(f"{i}. {j}") for i, j in enumerate(ls)]
    return input("메뉴 입력 : ")


def new_fruits_df():
    dict = {}
    schema = ['제품', '가격', '판매량']
    fruits = ['사과', '딸기', '수박']
    prices = [1800, 1500, 3000]
    sales = [24, 38, 13]
    for i, j in enumerate(schema):
        dict[j] = (fruits, prices, sales)[i]
    df = pd.DataFrame.from_dict(dict, orient='index')
    df = df.transpose()
    print(df)
    print('가격 평균: '+str(df['가격'].mean()))
    print('판매량 평균: '+str(df['판매량'].mean()))


def my_list(a, b):
    return list(range(a, b))


def new_number_2d():
    num_10 = my_list(10, 20)
    num_20 = my_list(20, 30)
    num_30 = my_list(30, 40)
    alphabet_list = list(string.ascii_lowercase)
    df = pd.DataFrame(np.array([num_10,
                                num_20,
                                num_30]),
                      columns=alphabet_list[0:10])
    print(df)


if __name__ == '__main__':
    while True:
        menu = fruit_menu(MENUS)
        if menu == "0":
            print(MENUS[0])
            break
        elif menu == "1":
            print(MENUS[1])
            new_fruits_df()
        elif menu == "2":
            print(MENUS[2])
            new_number_2d()
        else:
            print("잘못된 입력")
