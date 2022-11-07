from dataclasses import dataclass
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""

"""
class BugsMusic:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        ranks = soup.find_all(name='div', attrs={'class':'ranking'})
        titles = soup.find_all(name='p', attrs={'class':'title'})
        artists = soup.find_all(name='p', attrs={'class':'artist'})
        [print(f"{n0.find('strong').text}위 : {n1.find('a').text} by {n2.find('a').text}")
         for n0, n1, n2 in zip(ranks, titles, artists)]



class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')
        ranks = soup.find_all(name='span', attrs={'class':'rank'})
        titles = soup.find_all(name='div', attrs={'class':'ellipsis rank01'})
        artists = soup.find_all(name='span', attrs={'class':'checkEllipsis'})
        [print(f"{n0.text}위 : {n1.find('a').text} by {n2.find('a').text}")
         for n0, n1, n2 in zip(ranks[1:101], titles, artists)]
"""

@dataclass
class MusicRanking:
    html : str
    parser : str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname : str
    class_names : list
    artists : list
    titles : list
    dic : dict
    df : None

    @property
    def html(self) -> str: return self._html

    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self) -> str: return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def domain(self) -> str: return self._domain

    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self) -> str: return self._query_string

    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self) -> str: return self._headers

    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self) -> str: return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self) -> list: return self._class_names

    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self) -> list: return self._artists

    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self) -> list: return self._titles

    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def dic(self) -> dict: return self._dic

    @dic.setter
    def dic(self, dic): self._dic = dic

    @property
    def df(self) -> None: return self._df

    @df.setter
    def df(self, df): self._df = df

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_scv(self):
        path = CTX + self.fname + '.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
