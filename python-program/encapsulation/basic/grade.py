"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""


class Avg(object):
    def __init__(self, name, lang, eng, math) -> None:
        self.name = name
        self.lang = lang
        self.eng = eng
        self.math = math

    def get_total(self):
        lang = self.lang
        eng = self.eng
        math = self.math
        return lang + eng + math

    def get_avg(self):
        return self.get_total() / 3

    def get_grade(self):
        avg = self.get_avg()
        if avg >= 90:
            grade = "A학점"
        elif avg >= 80:
            grade = "B학점"
        elif avg >= 70:
            grade = "C학점"
        elif avg >= 60:
            grade = "D학점"
        elif avg >= 50:
            grade = "E학점"
        else:
            grade = "F학점"
        return grade
        
    def print_info(self):
        print(f"{self.name} {self.lang} {self.eng} {self.math} "
              f"{self.get_avg()} {self.get_total()} {self.get_grade()}")

    @staticmethod
    def new_grade():
        name = input("이름 : ")
        lang = int(input("국어점수 : "))
        eng = int(input("영어점수 : "))
        math = int(input("수학점수 : "))
        return Avg(name, lang, eng, math)

    @staticmethod
    def print_grade(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def print_menu():
        print("1. 성적 등록")
        print("2. 성적표")
        print("3. 성적 삭제")
        print("4. 종료")
        return int(input("메뉴 선택 :"))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Avg.print_menu()
            if menu == 1:
                print("### 성적 등록 ###")
                avg = Avg.new_grade()
                ls.append(avg)
            elif menu == 2:
                print("### 성적표 ###")
                print("*" * 35)
                print("이름 국어 영어 수학 총점 평균 학점")
                print("*" * 35)
                Avg.print_grade(ls)
                print("*" * 35)
            elif menu == 3:
                print("### 성적 삭제 ###")
            elif menu == 4:
                print("성적표 관리 어플을 종료합니다.")
                break


Avg.main()
