from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.url), arg.parser)
    ranks = soup.find_all(name='div', attrs={'class': 'ranking'})
    titles = soup.find_all(name=arg.tag_name, attrs={'class': arg.class_names[0]})
    artists = soup.find_all(name=arg.tag_name, attrs={'class': arg.class_names[1]})
    # 디버깅
    [print(f"{n0.find('strong').text}위 : {n1.find('a').text} by {n2.find('a').text}")
     for n0, n1, n2 in zip(ranks, titles, artists)]
    # dict 로 변환
    for i in range(0, len(titles)):
        arg.dic[arg.titles[i]] = arg.artists[i]

    # scv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_scv()



