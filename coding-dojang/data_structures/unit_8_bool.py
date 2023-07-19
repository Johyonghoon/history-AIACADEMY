def prac_pass_test():
    korean = 92
    english = 47
    mathematics = 86
    science = 81
    print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)


def test_pass_test():
    print("국어, 영어, 수학, 과학 점수를 입력하세요 : ")
    ko, en, ma, sc = map(int, input().split())
    print(ko >= 90 and en > 80 and ma > 85 and sc >= 80)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print('종료')
            break
        elif menu == '1':
            print('### 연습문제 : 합격 여부 출력하기 ###')
            prac_pass_test()
        elif menu == '2':
            print('### 심사문제 : 합격 여부 출력하기 ###')
            test_pass_test()
        else:
            print('메뉴를 다시 입력하세요.')
