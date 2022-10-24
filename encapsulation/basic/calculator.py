class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def execute(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "잘못된 연산입니다."
        print(f"{num1} {op} {num2} = {result}")

    @staticmethod
    def print_menu():
        print("### 목록 ###")
        print("1. 연산 등록")
        print("2. 연산 목록")
        print("3. 연산 삭제")
        print("0. 연산 종료")
        return input("원하는 메뉴의 번호를 입력하세요.")

    @staticmethod
    def main():
        # ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 0:
                print("### 연산 종료 ###")
                break
            elif menu == 1:
                print("### 연산 등록 ###")
            elif menu == 2:
                print("### 연산 목록 ###")
            elif menu == 3:
                print("### 연산 삭제 ###")
            else:
                print("없는 메뉴입니다. 다시 선택해 주세요")


Calculator.main()
