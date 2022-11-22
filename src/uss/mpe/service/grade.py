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


class Grade(object):

    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma

    def print(self):
        pass

    @staticmethod
    def new_grade():
        return Grade(input("이름 : "),
                     int(input("국어성적 : ")),
                     int(input("영어성적 : ")),
                     int(input("수학성적 : ")))

    def get_sum(self):
        return self.ko + self.en + self.ma

    def get_avg(self):
        return self.get_sum() / 3

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
        return f"{self.name} {self.ko} {self.en} {self.ma} {self.get_sum()} {self.get_avg()} {self.get_grade()}"

    @staticmethod
    def print_grades(ls):
        for i in ls:
            print(i)

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
