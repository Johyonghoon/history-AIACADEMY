from util.menu import Menu


class Bubble(object):

    def __init__(self):
        pass

    def print(self):
        pass

    @staticmethod
    def new_bubble():
        return Bubble(input(""),
                      input(""),
                      input(""))

    @staticmethod
    def print_bubbles():
        pass

    @staticmethod
    def delete_bubble():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Menu.print_menu()
            if menu == 1:
                print("### 입력 ###")
                bubble = Bubble.new_bubble()
                ls.append(bubble)
            elif menu == 2:
                print("### 출력 ###")
                Bubble.print_bubbles()
            elif menu == 3:
                print("### 삭제 ###")
                Bubble.delete_bubble()
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("잘못된 접근입니다.")


Bubble.main()

