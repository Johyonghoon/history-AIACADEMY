class Calculator(object):
    def __init__(self):
        pass

    def print(self):
        print("")

    @staticmethod
    def print_menu():
        pass

    @staticmethod
    def new_calculator():
        pass

    @staticmethod
    def print_calculator():
        pass

    @staticmethod
    def delete_calculator():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 1:
                print("### 계산 입력 ###")
                Calculator.new_calculator()
            elif menu == 2:
                print("### 계산 목록 ###")
                Calculator.print_calculator()
            elif menu == 3:
                print("### 계산 삭제 ###")
                Calculator.delete_calculator()
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("잘못된 번호입니다. 다시 입력하세요.")

Calculator.main()