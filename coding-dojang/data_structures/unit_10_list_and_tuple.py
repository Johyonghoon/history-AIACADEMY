def prac_list_range():
    a = list(range(5, -10, -2))
    print(a)


def test_list_range():
    gap = int(input("증가시키고자 하는 숫자를 입력하세요 : "))
    a = tuple(range(-10, 10, gap))
    print(a)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print('### 연습문제 : range로 리스트 만들기 ###')
            prac_list_range()
        elif menu == "2":
            print('### 심사문제 : range로 리스트 만들기 ###')
            test_list_range()
        else:
            print("메뉴를 다시 입력하세요.")