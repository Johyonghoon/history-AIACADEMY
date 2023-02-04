class Annie:
    def __init__(self, hp, mp, ap):
        self.hp = hp
        self.mp = mp
        self.ap = ap

    def tibbers(self):
        print(f"티버: 피해량 {ap * 0.65 + 400}")


class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("베기")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 게임 캐릭터 클래스 만들기 ###")
            print("게임 캐릭터 능력치(체력, 마나, AP)를 입력하세요.")
            hp, mp, ap = map(float, input().split())
            x = Annie(hp=hp, mp=mp, ap=ap)
            x.tibbers()
        elif menu == '2':
            print("### 심사문제 : 게임 캐릭터 클래스 만들기 ###")
            x = Knight(health=542.4, mana=210.3, armor=38)
            print(x.health, x.mana, x.armor)
            x.slash()

