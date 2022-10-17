class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        if self.op == "+":
            print(f"{self.num1} {self.op} {self.num2} = {self.num1 + self.num2}")
        if self.op == "-":
            print(f"{self.num1} {self.op} {self.num2} = {self.num1 - self.num2}")
        if self.op == "*":
            print(f"{self.num1} {self.op} {self.num2} = {self.num1 * self.num2}")
        if self.op == "/":
            print(f"{self.num1} {self.op} {self.num2} = {self.num1 / self.num2}")
        elif self.op == "%":
            print(f"{self.num1} {self.op} {self.num2} = {self.num1 % self.num2}")

if __name__=="__main__":
    num1 = int(input("숫자 : "))
    op = input("+ - * / %")
    num2 = int(input("숫자 : "))
    calculator = Calculator(num1, op, num2)
    calculator.calc()