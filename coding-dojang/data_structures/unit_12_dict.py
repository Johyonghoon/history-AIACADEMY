def prac_dict():
    camille = {
        'health' : 575.6,
        'health_regen' : 1.7,
        'mana' : 338.8,
        'mana_regen' : 1.63,
        'melee' : 125,
        'attack_damage' : 60,
        'attack_speed' : 0.625,
        'armor' : 26,
        'magic_resistance' : 32.1,
        'movement_speed' : 340
    }
    print(camille['health'])
    print(camille['movement_speed'])


def judge_dict():
    print("게임 캐릭터의 키와 값을 각각 입력하세요.")
    key = list(input().split())
    value = list(input().split())
    dc = dict(zip(key, value))
    print(dc)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 딕셔너리 게임 캐릭터 능력치 저장 ###")
            prac_dict()
        elif menu == '2':
            print("### 심사문제 : 딕셔너리 게임 캐릭터 능력치 저장 ###")
            judge_dict()
