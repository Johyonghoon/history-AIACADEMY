def prac_for():
    x = [49, -17, 25, 102, 8, 62, 21]
    for i in x:
        print(i * 10, end=' ')
    print()


def judge_for_range_multiplication_table():
    print("알고자 하는 구구단의 정수를 입력하세요. ")
    num = int(input())
    for i in range(10):
        print(f"{num} * {i} = {num * i}")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 리스트 요소에 10을 곱하여 출력 ###")
            prac_for()
        elif menu == '2':
            print("### 심사문제 : 구구단 출력 ###")
            judge_for_range_multiplication_table()
        else:
            print("다시 입력하세요. ")