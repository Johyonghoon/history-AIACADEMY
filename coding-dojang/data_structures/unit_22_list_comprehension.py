def prac_list_comp():
    a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
    b = [i for i in a if len(i) == 5]
    print(b)


def judge_list_comp():
    print("2의 거듭제곱을 확인하고 싶은 범위의 두 수를 입력하세요.")
    a, b = map(int, input().split())
    ls = list(range(a, b+1))
    ls2 = []
    if 1 <= a <= 20 and 10 <= b <= 30 and a < b:
        for i, j in enumerate(ls):
            if i == 1 or i == (len(ls)-2):
                continue
            ls2.append(2 ** j)
        print(ls2)
    else:
        print("범위를 벗어났습니다. 다시 입력하세요.")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 리스트 특정요소 뽑아내기 ###")
            prac_list_comp()
        elif menu == '2':
            print("### 심사문제 : 2의 거듭제곱 리스트 생성 ###")
            judge_list_comp()
        else:
            print("다시 입력하세요. ")

