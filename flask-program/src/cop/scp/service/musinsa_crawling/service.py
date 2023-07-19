from urllib.request import urlopen

from bs4 import BeautifulSoup


def musinsa_crawling(arg):
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


if __name__ == '__main__':
    print("무신사 크롤링")
    scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
    scrap.query_string = "20221106"
    scrap.parser = "lxml"
    scrap.class_names = ["title", "artist"]
    scrap.tag_name = "p"
    musinsa_crawling(scrap)