def prac_recursive_func_palindrome():
    pass

    # print(is_palindrome('hello'))
    # print(is_palindrome('level'))


def judge_fibonacci_num():
    pass


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 재귀 호출로 회문 판별 ###")
            prac_recursive_func_palindrome()
        elif menu == '2':
            print("### 심사문제 : 재귀 호출로 피보나치 수 구하기 ###")
            judge_fibonacci_num()
        else:
            print("다시 입력하세요. ")