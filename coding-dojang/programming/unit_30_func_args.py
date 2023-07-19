def get_max_score(*args):
    return max(args)


def prac_func_arg():
    ko, en, ma, sc = 100, 86, 81, 91
    max_score = get_max_score(ko, en, ma, sc)
    print(f"높은 점수: {max_score}")
    max_score = get_max_score(en, sc)
    print(f"높은 점수: {max_score}")


def get_min_max_score(*args):
    return min(args), max(args)


def get_average(*args):
    return sum(args) / len(args)


def judge_func_arg():
    print("국어, 영어, 수학, 과학 점수를 입력하세요. ")
    ko, en, ma, sc = map(int, input().split())

    min_score, max_score = get_min_max_score(ko, en, ma, sc)
    average_score = get_average(ko, en, ma, sc)
    print(f"낮은 점수:{min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수:{average_score:.2f}")

    min_score, max_score = get_min_max_score(en, sc)
    average_score = get_average(en, sc)
    print(f"낮은 점수:{min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수:{average_score:.2f}")

if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 가장 높은 점수를 구하는 함수 만들기 ###")
            prac_func_arg()
        elif menu == '2':
            print("### 심사문제 : 가장 낮은 점수, 높은 점수와 평균을 구하는 함수 만들기 ###")
            judge_func_arg()
        else:
            print("다시 입력하세요. ")

