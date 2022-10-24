"""
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
"""


class Bmi(object):

    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    def print(self):
        print("")
        pass

    @staticmethod
    def print_menu():
        print("### 메뉴 ###")
        print("1. 개인정보 입력")
        print("2. 비만도 목록")
        print("3. 개인정보 삭제")
        print("### 종료 ###")
        return int(input("목록 선택 : "))

    @staticmethod
    def new_condi():
        return Bmi(input("이름 : "),
                   int(input("키(cm) : ")),
                   int(input("몸무게(kg) : ")))

    def get_bmi(self):
        m = self.cm / 100
        return self.kg / m ** 2

    def get_biman(self):
        bmi = self.get_bmi()
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        return biman

    def print_info(self):
        print(f"{self.name} {self.cm} {self.kg} {self.get_biman()}")

    @staticmethod
    def print_condis(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def delete_condi(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("### Bmi 등록 ###")
                bmi = Bmi.new_condi()
                ls.append(bmi)
            elif menu == 2:
                print("### Bmi 목록 ###")
                Bmi.print_condis(ls)
            elif menu == 3:
                print("### Bmi 삭제 ###")
                Bmi.delete_condi(ls, input("삭제할 이름 : "))
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")


Bmi.main()
