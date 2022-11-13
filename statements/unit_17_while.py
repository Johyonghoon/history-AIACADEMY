def prac_while():
    i = 2
    j = 5
    while i <= 32 and 1 <= j:
        print(i, j)
        i = i * 2
        j = j - 1


def judge_while():
    print("금액을 입력하세요. ")
    balance = int(input())
    while balance >= 1350:
        balance -= 1350
        print(balance)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 변수 두 개를 다르게 반복 ###")
            prac_while()
        elif menu == '2':
            print("### 심사문제 : 교통카드 잔액 출력 ###")
            judge_while()
        else:
            print("다시 입력하세요. ")
