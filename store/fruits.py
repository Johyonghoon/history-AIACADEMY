import pandas as pd


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
    print('가격평균: '+str(df['가격'].mean()))
    print('판매량평균: '+str(df['판매량'].mean()))


if __name__ == '__main__':
    new_fruits_df()
