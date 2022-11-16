def prac_three_dimensional_list():
    a = [[[0 for i in range(3)] for j in range(4)] for k in range(2)]
    print(a)


def judge_minesweeper():
    pass # TODO : 고민 많이 해보기


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 3차원 리스트 만들기 ###")
            prac_three_dimensional_list()
        elif menu == '2':
            print("### 심사문제 : 지뢰찾기 ###")
            judge_minesweeper()
        else:
            print("다시 입력하세요. ")
