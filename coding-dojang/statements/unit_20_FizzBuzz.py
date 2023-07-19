def prac_fizzbuzz_2_11():
    for i in range(1, 101):
        if i % 2 == 0 and i % 11 == 0:
            print("FizzBuzz")
        elif i % 2 == 0:
            print("Fizz")
        elif i % 11 == 0:
            print("Buzz")
        else:
            print(i)


def judge_fizzbuzz_5_7():
    start, stop = map(int, input().split())
    if 1 < start < 1000 and 10 < stop < 1000 and start < stop:
        for i in range(start, stop+1):
            if i % 5 == 0 and i % 7 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Fizz")
            elif i % 7 == 0:
                print("Buzz")
            else:
                print(i)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 2와 11의 배수, 공배수 처리하기 ###")
            prac_fizzbuzz_2_11()
        elif menu == '2':
            print("### 심사문제 : 5와 7의 배수, 공배수 처리하기 ###")
            judge_fizzbuzz_5_7()
        else:
            print("다시 입력하세요. ")
