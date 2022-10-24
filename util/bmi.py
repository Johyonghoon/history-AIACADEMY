'''
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
'''
class Bmi(object):
    def __init__(self):
        pass

    def print(self):
        print("")

    @staticmethod
    def print_menu():
        pass

    @staticmethod
    def new_info():
        pass

    @staticmethod
    def print_infos():
        pass

    @staticmethod
    def delete_info():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("### Bmi 등록 ###")
                bmi = Bmi.new_info()
            elif menu == 2:
                print("### Bmi 목록 ###")
                bmi = Bmi.print_infos()
            elif menu == 3:
                print("### Bmi 삭제 ###")
                bmi = Bmi.delete_info()
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")

Bmi.main()