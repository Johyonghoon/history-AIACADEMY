import string


def prac_string_path():
    path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
    ls = path.split('\\')
    filename = ls[-1]
    print(filename)


def judge_string_count():
    print("'the' 갯수를 출력할 문자열을 입력하세요. ")
    value = input().strip(string.punctuation)
    ls_value = value.split()
    print(ls_value.count('the'))


def judge_string_assignment():
    print("물품 가격을 ;(세미콜론)으로 구분하여 나열하세요. ")
    ls_price = input().split(';')
    ls_price_int = list(map(int, ls_price))
    ls_price_int.sort(reverse=True)
    [print('%9s' % format(i, ',')) for i in ls_price_int]


if __name__ == '__main__':
    while True:
        menu = input('메뉴 입력 : ')
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 파일 경로에서 파일명만 가져오기 ###")
            prac_string_path()
        elif menu == '2':
            print("### 심사문제 : 특정 단어 개수 세기 ###")
            judge_string_count()
        elif menu == '3':
            print("### 심사문제 : 높은 가격순으로 출력하기 ###")
            judge_string_assignment()
        else:
            print("다시 입력하세요. ")
