import os
import random

import pandas as pd
from sqlalchemy import create_engine

from api.path import dir_path
from exrc.algorithms.lambdas import lambda_number, lambda_k_name, lambda_string, lambda_phone, lambda_birth, \
    address_list, job_list, interests_list


class UsersService:
    def __init__(self):
        global id, email, nickname, passwd, wordlist
        id = None
        email = None
        nickname = None
        passwd = None
        wordlist = os.path.join(dir_path("exrc_users"), "data", "wordlist.txt")

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
        print("포스트맨의 요청이 도달하였음 !! ")

    def create_hunnit_acc_in_df(self):
        columns = ['user_id', 'user_email', 'password', 'user_name', 'phone', 'birth',
                   'address', 'job', 'user_interests', 'token']
        df = pd.DataFrame(data=None, columns=columns)
        for i in range(100):
            dummy_acc = {'user_id': f'{self.get_random_word() + lambda_number(4)}',
                         'user_email': f'{lambda_string(5) + lambda_number(4)}@gmail.com',
                         'password': '1',
                         'user_name': f"{lambda_k_name(3)}",
                         'phone': f"{lambda_phone(4)}",
                         'birth': f"{lambda_birth(1985, 2011)}",
                         'address': f"{random.choice(address_list)}",
                         'job': f"{random.choice(job_list)}",
                         'user_interests': f"{random.choice(interests_list)}",
                         'token': 'JWT fefege..'
                         }
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

