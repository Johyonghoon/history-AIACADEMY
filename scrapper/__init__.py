from scrapper.domains import Scrap
from scrapper.views import ScrapperController
from util.menu import Menu

if __name__ == '__main__':

    api = ScrapperController()
    scrap = Scrap()

    while True:
        menus = ["종료", "벅스 뮤직", "멜론"]
        menu = Menu.menu(menus)
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
            api.menu_1_bugsMusic(scrap)
        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm"
            scrap.parser = "lxml"
            scrap.class_names = ['ellipsis rank01', 'checkEllipsis']
            api.menu_2_melon(scrap)
            scrap.class_names = ["title", "artist"]
        else:
            print("잘못된 접근")


