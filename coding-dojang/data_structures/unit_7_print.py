def prac_print_date_and_time():
    year = 2000
    month = 10
    day = 27
    hour = 11
    minute = 43
    second = 59
    print(year, month, day, sep='/', end='')
    print(hour, minute, second, sep=':')


def test_print_date_and_time():
    year, month, day, hour, minute, second = map(int, input("년 월 일 시 분 초를 입력하세요 : ").split())
    print(year, month, day, sep='-', end='T')
    print(hour, minute, second, sep=':')


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("### 연습문제 : 날짜와 시간 출력하기 ###")
            prac_print_date_and_time()
        elif menu == "2":
            print("### 심사문제 : 날짜와 시간 출력하기 ###")
            test_print_date_and_time()
