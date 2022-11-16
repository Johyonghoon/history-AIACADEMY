def prac_lambda():
    files = ['fonts', '1.png', '10.png', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
    print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))


def judge_lambda():
    files = input().split()
    # lambda x :  ,files


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력")
        if menu =='0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 이미지 파일만 가져오기 ###")
            prac_lambda()
        elif menu == '2':
            print("### 심사문제 : 파일 이름 한 번에 바꾸기 ###")
            judge_lambda()
        else:
            print("다시 입력하세요. ")
