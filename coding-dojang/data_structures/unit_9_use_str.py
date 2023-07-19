def prac_sev_str():
    s = """Python is a programming language that lets you work quickly
    and
    integrate systems more effectivly."""
    print(s)


def test_sev_str():
    s = """'Python' is a \"programming language\"
    that lets you work quickly
    and integrate systems more effectively."""
    print(s)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("### 연습문제 : 여러 줄로 된 문자열 사용하기 ###")
            prac_sev_str()
        elif menu == "2":
            print("### 심사문제 : 여러 줄로 된 문자열 사용하기 ###")
            test_sev_str()


# 출력 결과가 앞에 blank가 들어간 상태로 나오는데 어떻게 조치?
