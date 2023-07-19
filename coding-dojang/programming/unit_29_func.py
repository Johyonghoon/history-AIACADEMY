def get_quotient_remainder(a, b):
    return a // b , a % b


def prac_func():
    x = 10
    y = 3
    quotient, remainder = get_quotient_remainder(x, y)
    print(f"몫 : {quotient}, 나머지 : {remainder}")


def calc(x, y):
    return x+y, x-y, x*y, x/y


def judge_func():
    print("사칙연산을 하고자 하는 두 수를 입력하세요. ")
    x, y = map(int, input().split())
    a, s, m, d = calc(x, y)
    print(f"덧셈 : {a}, 뺄셈 : {s}, 곱셈 : {m}, 나눗셈 : {d}")

if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 몫과 나머지를 구하는 함수 만들기 ###")
            prac_func()
        elif menu == '2':
            print("### 심사문제 : 사칙 연산 함수 만들기 ###")
            judge_func()
        else:
            print("다시 입력하세요. ")
