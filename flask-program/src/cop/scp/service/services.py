import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup


def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    ranks = soup.find_all(name='div', attrs={'class': 'ranking'})
    ranks = [i. find('strong').text for i in ranks]
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


def Melon(arg):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(arg.domain, headers= headers)
    soup = BeautifulSoup(urlopen(req), arg.parser)
    ranks = soup.find_all(name='span', attrs={'class':'rank'})
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
