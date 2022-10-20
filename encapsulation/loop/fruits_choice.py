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
class Menu(object):
    def __init__(self,fruits) -> None:
        self.menu = ["바나나", "사과", "망고"]
        self.fruits = fruits

    def print_menu(self):
        fruits = self.fruits
        k = []
        for i in self.menu :
            if fruits == '"바"':
                print(f'구매할 과일 : {i}')
                break
            elif fruits == "사":
                print(f'구매할 과일 : {i}')
                break
            elif fruits == "망":
                print(f'구매할 과일 : {i}')
                break
            else:
                k.append(i)
                if len(k) == 3:
                    print("찾으시는 과일은 저희 매장에서 판매하지 않습니다.")
                    '''
                    print("### 과일번호표 ###")
                    print("*" * 40)
                    k=0
                    for i in self.menu :
                        print(f"{k+1}번 과일 : {i}")
                        k += 1
                    print("*" * 40)
    '''
    @staticmethod
    def main():
        fruits = input("구매할 과일의 첫글자를 입력하세요.")
        menu = Menu(fruits)
        menu.print_menu()

Menu.main()