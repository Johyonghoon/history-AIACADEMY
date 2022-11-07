from scrapper.domains import MusicRanking
from scrapper.views import ScrapperController
from util.menu import Menu

if __name__ == '__main__':

    api = ScrapperController()
    m = MusicRanking()

    while True:
        menus = ["종료", "벅스 뮤직", "멜론"]
        menu = Menu.menu(menus)
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스 뮤직")
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221106"
            m.parser = "lxml"
            m.class_names.append("title")
            m.class_names.append("artist")
            m.tag_name = "p"
            api.menu_1(m)
        elif menu == "2":
            print("멜론")
            api.menu_2_melon(arg="https://www.melon.com/chart/index.htm")
        else:
            print("잘못된 접근")


