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
        self.grade = ""

    def execute(self):
        self.grade = self.get_grade()
        self.get_grade()
        self.print_grade()

    def get_total(self):
        lang = self.lang
        eng = self.eng
        math = self.math
        return lang + eng + math

    def get_avg(self):
        total = self.get_total()
        return total / 3

    def get_grade(self):
        grade=""
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
        self.grade = grade
        
        
    def print_grade(self):
        name = self.name
        lang = self.lang
        eng = self.eng
        math = self.math
        avg = round(self.get_avg())
        total = self.get_total()
        grade = self.grade
        title = "### 성적표 ###"
        aster = "*" * 40
        schema = "이름 국어 영어 수학 총점 평균 학점"
        result = f"{name} {lang} {eng} {math} {avg} {total} {grade}"
        print(f'{title} \n {aster} \n {schema} \n {aster} \n {result} \n {aster}')

    @staticmethod
    def main():
            name = input("이름 : ")
            lang = int(input("국어점수 : "))
            eng = int(input("영어점수 : "))
            math = int(input("수학점수 : "))
            avg = Avg(name, lang, eng, math)
            avg.execute()

Avg.main()