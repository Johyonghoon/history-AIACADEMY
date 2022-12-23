import random

import pandas as pd
from sqlalchemy import create_engine

class UsersService:
    def __init__(self):
        global id, email, nickname, passwd, wordlist
        id = None
        email = None
        nickname = None
        passwd = None
        wordlist = r"C:\Users\AIA\PycharmProjects\djangoProject\exrc\auth\exrc_users\data\wordlist.txt"

    def create_acc_hook(self):
        hunnit_acc = self.create_hunnit_acc_in_df()
        self.create_df_in_mydb(hunnit_acc)

    def get_random_word(self):
        with open(wordlist, 'r', encoding='utf-8') as f:
            words = f.read().splitlines()
        return random.choice(words)

    """
    def create_account(self):
        dummy_acc = {'id': f'{self.get_random_word()}',
                     'email': f'{self.get_random_word()}@gmail.com',
                     'nickname': f"{self.get_random_word()}",
                     'passwd': '0'}
        # if dummy_acc ==
        """

    def get_accounts(self):
        pass

    def create_hunnit_acc_in_df(self):
        columns = ['id', 'email', 'nickname', 'passwd']
        df = pd.DataFrame(data=None, columns=columns)
        for i in range(100):
            dummy_acc = {'id': f'{self.get_random_word()}',
                         'email': f'{self.get_random_word()}@gmail.com',
                         'nickname': f"{self.get_random_word()}",
                         'passwd': '0'}
            df = df.append(dummy_acc, ignore_index=True)
        print(df)
        return df

    def create_df_in_mydb(self, hunnit_acc):
        df = hunnit_acc
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='exrc_users',
                  if_exists='append',
                  con=engine,
                  index=False)


if __name__ == '__main__':
    service = UsersService()
    service.create_acc_hook()

