def prac_closure():
    def counter():
        i = 0
        def count():
            nonlocal i
            i += 1
            return i
        return count
    c = counter()
    for i in range(10):
        print(c(), end=' ')


def judge_closure():
    def countdown(n):

        def c(n):
            nonlocal i
    n = int(input())

    c = countdown(n)
    for i in range(n):
        print(c(), end=' ')



if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 호출 횟수를 세는 함수 만들기 ###")
            prac_closure()
        elif menu == '2':
            print("### 심사문제 : 카운트 함수 만들기 ###")
            judge_closure()
        else:
            print("다시 입력하세요. ")

