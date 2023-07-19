def prac_if():
    x = 5
    if x != 10:
        print("ok")


def judge_if():
    print("가격과 할인쿠폰을 각각 입력하세요.")
    price = int(input())
    coupon = input()
    if coupon == "Cash3000":
        print(f"할인 가격 : {price - 3000}")
    if coupon == "Cash5000":
        print(f"할인 가격 : {price - 5000}")


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : if 조건문 사용 ###")
            prac_if()
        elif menu == '2':
            print("### 심사문제 : 온라인 할인 쿠폰 시스템 만들기 ###")
            judge_if()
        else:
            print("다시 입력하세요. ")

