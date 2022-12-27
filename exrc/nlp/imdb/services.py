import csv
import time
from os import path

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from exrc.nlp.imdb.models import Imdb_model


class Imdb_service:
    def __init__(self):
        model = Imdb_model().create_rnn_model()

    def imdb_hook(self):
        model = Imdb_model()
        model.fit()


class NaverMovieService(object):
    def __init__(self):
        global url, chrome_driver, driver, savepath, character_set
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page='
        chrome_driver = r'C:\Users\AIA\PycharmProjects\djangoProject\exrc\webcrawler\chromedriver.exe'
        driver = webdriver.Chrome(chrome_driver)
        savepath = './naver_movie_review_corpus.csv'
        character_set = "UTF-8"

    def crawling(self):
        if not path.exists(savepath):
            review_data = []
            for page in range(1, 2):
                driver.get(url + str(page))
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                all_tds = soup.find_all('td', attrs={'class', 'title'})
                for review in all_tds:
                    need_reviews_cnt = 1000
                    sentence = review.find("a", {"class": "report"}).get("onclick").split("', '")[2]
                    if sentence != "":  # 리뷰 내용이 비어있다면 데이터를 사용하지 않음
                        score = review.find("em").get_text()
                        review_data.append([sentence, int(score)])
            time.sleep(1)  # 다음 페이지를 조회하기 전 1초 시간 차를 두기
            with open(savepath, 'w', newline='', encoding=character_set) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()

        data = pd.read_csv(savepath, header=None)
        data.columns = ['review', 'score']
        result = [print(f"{i + 1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
        return result


if __name__ == '__main__':
    # service = Imdb_service()
    # service.imdb_hook()
    NaverMovieService().crawling()
