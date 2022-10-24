"""
과일 판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
첫 글자를 입력했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
*******************************
1번 과일 : 바나나
2번 과일 : 사과
3번 과일 : 망고
********************************
ex) 구매할 과일 : 바
"""


class Fruits(object):

    def __init__(self) -> None:
        self.menu = ["바나나", "사과", "망고"]

    def print_menu(self):
        print("### 과일번호표 ###")
        print("********************************")
        j = 0
        for i in self.menu:
            print(f"{j + 1}번과일: {i}")
            j += 1
        print("********************************")

    @staticmethod
    def main():
        fruits = Fruits()
        fruits.print_menu()


Fruits.main()
