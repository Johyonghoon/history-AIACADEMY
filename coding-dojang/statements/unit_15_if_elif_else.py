def prac_if_elif_else():
    x = int(input())
    if 11 <= x <= 20:
        print("11~20")
    elif 21 <= x <= 30:
        print("21~30")
    else:
        print("아무것도 해당하지 않음")


def judge_if_elif():
    print("만 나이를 입력하세요. :")
    age = int(input())
    balance = 9000
    if 7 <= age <= 12:
        balance -= 650
    elif 13 <= age <= 18:
        balance -= 1050
    elif 19 <= age:
        balance -= 1250
    print(balance)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : if, elif, else 모두 사용 ###")
            prac_if_elif_else()
        elif menu == '2':
            print("### 심사문제 : 교통카드 시스템 만들기 ###")
            judge_if_elif()
        else:
            print("다시 입력하세요. ")
