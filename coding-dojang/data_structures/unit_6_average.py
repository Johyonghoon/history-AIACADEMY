def practice_input_split():
    a, b, c = map(int, input('숫자 3개를 입력하세요 : ').split())
    print(a+b+c)


def judge_variable():
    a = 50
    b = 100
    c = None
    print(a)
    print(b)
    print(c)


def judge_average():
    print('숫자 네 개를 입력하세요 : ')
    a, b, c, d = map(int, input().split())
    print(f"평균 점수 : {(a + b + c + d) / 4}")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 선택 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("### 연습문제 : 정수 3개 입력 후 합계 출력 ###")
            practice_input_split()
        elif menu == "2":
            print("### 심사문제 : 변수 만들기 ###")
            judge_variable()
        elif menu == "3":
            print("### 심사문제 : 평균 점수 구하기 ###")
            judge_average()
        else:
            print("메뉴를 다시 입력하세요.")

