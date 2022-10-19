class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):             # @가 안붙은 것은 다이나믹
        num1 = self.num1        # 코드를 간단하게 : 가독성 있게 만들어 줌
        op = self.op
        num2 = self.num2            
        if op == "+":
            result = num1 + num2
        elif op == "-":         # if와 달리 elif를 사용하면 앞의 if가 충족되었을 때 연산하지 않고 빠르게 넘어감
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
    
    @staticmethod                 # @는 장식자
    def main():
        num1 = int(input("숫자 : "))
        op = input("+ - * / %")
        num2 = int(input("숫자 : "))
        calculator = Calculator(num1, op, num2)
        calculator.calc()

Calculator.main()