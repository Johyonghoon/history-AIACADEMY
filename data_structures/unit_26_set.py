def prac_set():
    a = {i for i in range(1, 101) if i % 3 == 0}
    b = {i for i in range(1, 101) if i % 5 == 0}
    print(a & b)


def judge_set_intersection():
    a, b = map(int, input().split())
    a = {i for i in range(1, a+1) if a % i == 0}
    b = {i for i in range(1, b + 1) if b % i == 0}

    divisor = a & b

    result = 0
    if type(divisor) == set:
        result = sum(divisor)

    print(result)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("### 연습문제 : 공배수 구하기 ###")
            prac_set()
        elif menu == "2":
            print("### 심사문제 : 공약수 구하기 ###")
            judge_set_intersection()
        else:
            print("다시 입력하세요. ")
