import string


def prac_file():
    with open('./data/words.txt', 'r') as file:
        count = 0
        words = file.readlines()
        for word in words:
            if len(word.strip('\n')) <= 10:
                count += 1
        print(count)


def judge_file():
    with open('./data/words2.txt', 'r') as file:
        line = str(file.readline())
        ls = line.split()
        for i in ls:
            if 'c' in i:
                print(i.strip(string.punctuation))
        # TODO 16번 라인 다음에 line.strip(string.punctuation)을 처리하는 것은 왜 안되는지?


if __name__ == '__main__':
    while True:
        menu = input('메뉴 입력 : ')
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 파일에서 10자 이하인 단어 개수 세기 ###")
            prac_file()
        elif menu == '2':
            print("### 심사문제 : 특정 문자가 들어있는 단어 찾기 ###")
            judge_file()
        else:
            print("다시 입력하세요. ")
