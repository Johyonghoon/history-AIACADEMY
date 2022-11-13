def prac_slice():
    year = list(range(2011, 2019))
    population = [10249679, 10195318, 10143645, 10103233,
                  10022181, 9930616, 9857426, 9838892]
    print(year[-3:])
    print(population[-3:])


def prac_odd_index():
    n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
    print(n[1::2])


def judge_del_slice():
    ls = list(input().split())
    tu = tuple(ls[:-5])
    print(tu)


def judge_slice_concatenation():
    print("문자열 두 개를 차례대로 입력하세요. ")
    a = input()
    b = input()
    print(a[1::2] + b[::2])


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 최근 3년 간 인구 출력하기 ###")
            prac_slice()
        elif menu == '2':
            print("### 연습문제 : 인덱스 홀수인 요소 출력 ###")
            prac_odd_index()
        elif menu == '3':
            print("### 심사문제 : 리스트 마지막 부분 삭제 ###")
            judge_del_slice()
        elif menu == '4':
            print("### 심사문제 : 문자열 연결 ###")
            judge_slice_concatenation()
        else:
            print("다시 입력하세요. ")
