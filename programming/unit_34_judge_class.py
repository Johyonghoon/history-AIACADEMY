class Annie:
    def __init__(self, hp, mp, ap):
        self.hp = hp
        self.mp = mp
        self.ap = ap

    def tibbers(self):
        print(f"티버: 피해량 {ap * 0.65 + 400}")

    
if __name__ == '__main__':
    while True:
        print("게임 캐릭터 능력치(체력, 마나, AP)를 입력하세요.")
        hp, mp, ap = map(float, input().split())
        x = Annie(hp=hp, mp=mp, ap=ap)
        x.tibbers()
