def prac_if_else_multiple_cond_exp():
    written_test = 75
    coding_test = True
    if written_test >= 80 and coding_test == True:
        print('합격')
    else:
        print('불합격')


def judge_if_else_multiple_cond_exp():
    print("국어 영어 수학 과학 점수를 입력하세요.")
    ko, en, ma, sc = map(int, input().split())
    if ko > 100 or en > 100 or ma > 100 or sc >100:
        print("잘못된 점수")
    else:
        avg = (ko + en + ma + sc) / 4
        if avg >= 80:
            print("합격")
        else:
            print("불합격")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 합격 여부 판단 ###")
            prac_if_else_multiple_cond_exp()
        elif menu == '2':
            print("### 심사문제 : 합격 여부 판단 ###")
            judge_if_else_multiple_cond_exp()
