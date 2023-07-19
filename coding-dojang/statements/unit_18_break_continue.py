def prac_number_ending_3():
    i = 0
    while True:
        if i % 10 != 3:
            i += 1
            continue
        if i > 73:
            break
        print(i, end=' ')
        i += 1
    print()


def judge_exclude_number_ending_3():
    print("두 수를 입력하세요. ")
    start, stop = map(int, input().split())
    i = start
    if 1 <= start <= 200 and 10 <= stop <= 200 and start < stop:
        while True:
            if i % 10 == 3:
                i += 1
                continue
            if i > stop:
                break
            print(i, end=' ')
            i += 1
        print()
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 3으로 끝나는 숫자만 출력하기 ###")
            prac_number_ending_3()
        elif menu == '2':
            print("### 심사문제 : 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기 ###")
            judge_exclude_number_ending_3()
        else:
            print("다시 입력하세요. ")
