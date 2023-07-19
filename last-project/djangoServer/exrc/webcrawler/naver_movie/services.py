import csv
import os
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from api.path import dir_path
from exrc.webcrawler.naver_movie.models import ScrapModel


class ScrapService:

    def __init__(self):
        global driverpath, naver_url, savepath, character_set
        driverpath = os.path.join(dir_path("webcrawler"), "chromedriver.exe")
        savepath = os.path.join(dir_path("naver_movie"), "save", "movie_scrap.csv")
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        character_set = "UTF-8"

    def bugs_music(self, arg):  # BeautifulSoup 기본 크롤링
        soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
        ranks = soup.find_all(name='div', attrs={'class': 'ranking'})
        ranks = [i.find('strong').text for i in ranks]
        titles = soup.find_all(name=arg.tag_name, attrs={'class': arg.class_names[0]})
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs={'class': arg.class_names[1]})
        artists = [i.find('a').text for i in artists]
        # 디버깅
        [print(f'{i}위 : {j} by {k}') for i, j, k in zip(ranks, titles, artists)]
        # dict 로 변환
        diction = {}
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        # scv 파일로 저장
        arg.dict_to_dataframe()
        arg.dataframe_to_scv()

    def melon_music(self, arg):
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(arg.domain, headers=headers)
        soup = BeautifulSoup(urlopen(req), arg.parser)
        ranks = soup.find_all(name='span', attrs={'class': 'rank'})
        ranks = [i.text for i in ranks[1:101]]
        titles = soup.find_all(name='div', attrs={'class': arg.class_names[0]})
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name='span', attrs={'class': arg.class_names[1]})
        artists = [i.find('a').text for i in artists]
        [print(f'{i}위 : {j} by {k}') for i, j, k in zip(ranks, titles, artists)]
        diction = {}
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_scv()

    def naver_movie_review(self):
        if os.path.isfile(savepath) == False:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(savepath, 'w', newline='', encoding=character_set) as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
        title = pd.read_csv(savepath)
        result = [{'rank': f"{i+1}", 'title': f"{j}"} for i, j in enumerate(title)]
        return result


SCRAP_MENUS = ["종료",  # 0
               "Bugs Crawling",  # 1
               "Melon Crawling",  # 2
               "Naver Movie No.1",  # 3
               ]


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == '__main__':

    api = ScrapService()
    scrap = ScrapModel()

    while True:
        menu = my_menu(SCRAP_MENUS)
        if menu == "0":
            print("종료")
            break

        elif menu == "1":
            print("벅스 뮤직")
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221106"
            scrap.parser = "lxml"
            scrap.class_names = ["title", "artist"]
            scrap.tag_name = "p"
            api.bugs_music(scrap)

        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm"
            scrap.parser = "lxml"
            scrap.class_names = ['ellipsis rank01', 'checkEllipsis']
            api.melon_music(scrap)
            scrap.class_names = ["title", "artist"]

        elif menu == "3":
            print("### 네이버 영화 1등 표시 ###")
            api.naver_movie_review()
        else:
            print("잘못된 접근")


