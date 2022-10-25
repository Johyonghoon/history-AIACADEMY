class Fruits(object):

    def __init__(self):
        pass

    def print(self):
        pass

    @staticmethod
    def print_menu():
        pass

    @staticmethod
    def new_fruit():
        pass

    @staticmethod
    def print_fruits():
        pass

    @staticmethod
    def delete_fruit():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Fruits.print_menu()
            if menu == 1:
                print("### 입력 ###")
                fruit = Fruits.new_fruit()
                ls.append(fruit)
            elif menu == 2:
                print("### 출력 ###")
                Fruits.print_fruits()
            elif menu == 3:
                print("### 삭제 ###")
                Fruits.delete_fruit()
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("잘못된 접근입니다.")


Fruits.main()
