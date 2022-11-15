def prac_dict_avg():
    maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
    average = sum(maria.values()) / len(maria)
    print(average)


def judge_dict_del():
    keys = input().split()
    values = map(int, input().split())

    x = dict(zip(keys, values))
    del x['delta']
    x = {key: value for key, value in x.items() if value != 30}

    print(x)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("### 연습문제 : 평균 점수 구하기 ###")
            prac_dict_avg()
        elif menu == "2":
            print("### 심사문제 : 딕셔너리 특정 값 삭제 ###")
            judge_dict_del()
        else:
            print("다시 입력하세요. ")
