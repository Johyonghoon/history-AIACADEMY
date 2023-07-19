def prac_n_gram_word():
    n = int(input())
    text = input()
    words = text.split()

    if n > len(words):
        print('wrong')
    else:
        n_gram = zip(*[words[i:] for i in range(n)])
        for i in n_gram:
            print(i)


def judge_palindrome():
    with open('./data/words3.txt', 'r') as file:
        line = None
        while line !='':
            line = file.readline()
            line = line.strip('\n')
            if line == line[::-1]:
                print(line)


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu =='1':
            print("### 연습문제 : 단어 단위 N-gram 만들기 ###")
            prac_n_gram_word()
        elif menu =='2':
            print("### 심사문제 : 파일에서 회문인 단어 출력하기 ###")
            judge_palindrome()
        else:
            print("다시 입력하세요. ")
