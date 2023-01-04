import os

import numpy as np
import pandas as pd

from api.path import dir_path


class DataPreprocess:

    def __init__(self):
        global kospi_df, samsung_df
        kospi_df = pd.read_csv(os.path.join(dir_path("aitrader"), "data", "kospi200_220103_to_221229.csv"),
                               index_col=0, header=0, encoding='utf-8', sep=',')
        samsung_df = pd.read_csv(os.path.join(dir_path("aitrader"), "data", "samsung_220103_to_221229.csv"),
                               index_col=0, header=0, encoding='utf-8', sep=',')

    def data_preprocess_hook(self):
        # self.print_data()
        self.del_row_with_null_data()
        self.change_datatype()
        self.save_preprocessing_data()

    def print_data(self):
        print(f" --------------- KOSPI200 DATA ---------------\n{kospi_df}\n"
              f" --------------- KOSPI200 SHAPE ---------------\n{kospi_df.shape}\n"
              f" --------------- SAMSUNG DATA ---------------\n{samsung_df}\n"
              f" --------------- SAMSUNG SHAPE ---------------\n{samsung_df.shape}")

    def del_row_with_null_data(self):
        global samsung_df
        samsung_df = samsung_df.dropna(axis=0)

    def change_datatype(self):
        global kospi_df, samsung_df
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        for i in range(len(kospi_df.index)):
            if kospi_df.iloc[i, 4][-1] == 'M':
                kospi_df.iloc[i, 4] = int(float(kospi_df.iloc[i, 4][:-1]) * 1000000)
            elif kospi_df.iloc[i, 4][-1] == 'K':
                kospi_df.iloc[i, 4] = int(round(float(kospi_df.iloc[i, 4][:-1]) * 10000000))

        for i in range(len(samsung_df.index)):
            for j in range(0, 4):
                samsung_df.iloc[i, j] = int(samsung_df.iloc[i, j].replace(',', ''))
            if samsung_df.iloc[i, 4][-1] == 'M':
                samsung_df.iloc[i, 4] = int(float(samsung_df.iloc[i, 4][:-1]) * 1000000)
            elif samsung_df.iloc[i, 4][-1] == 'K':
                samsung_df.iloc[i, 4] = int(round(float(samsung_df.iloc[i, 4][:-1]) * 10000000))
        kospi_df = kospi_df.sort_values(['날짜'], ascending=[True]).drop(["변동 %"], axis=1)
        samsung_df = samsung_df.sort_values(['날짜'], ascending=[True]).drop(["변동 %"], axis=1)

    def save_preprocessing_data(self):
        precessed_kospi_df = kospi_df.values
        precessed_samsung_df = samsung_df.values
        print(precessed_kospi_df)
        print(precessed_samsung_df)
        np.save(os.path.join(dir_path("aitrader"), "save", "processed_kospi200.npy"), arr=precessed_kospi_df)
        np.save(os.path.join(dir_path("aitrader"), "save", "processed_samsung.npy"), arr=precessed_samsung_df)


if __name__ == '__main__':
    DataPreprocess().data_preprocess_hook()
