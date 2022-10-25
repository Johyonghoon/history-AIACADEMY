from util.menu import Menu


class Test(object):
    def __init__(self):
        pass

    @staticmethod
    def new_test():
        pass

    @staticmethod
    def all_tests():
        pass

    @staticmethod
    def delete_tests():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Menu.menu()
            if menu == 1:
                print("### 테스트 입력 ###")
                test = Test.new_test()
            elif menu == 2:
                print("### 테스트 목록 ###")
                test = Test.all_tests()
            elif menu == 3:
                print("### 테스트 삭제 ###")
                test = Test.delete_tests()
            elif menu == 0:
                print("### 종료 ###")
                break


Test.main()
