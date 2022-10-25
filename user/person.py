"""
이름, 주민번호(950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개어플 ###
*******************************
이름 : 홍길동
나이 : 25살(만나이)
성별 : 남성
주소 : 서울
********************************
"""


class Person(object):

    def __init__(self, name, num, addr):
        self.name = name
        self.num = num
        self.addr = addr
        self.set_age()
        self.set_gen()

    def set_age(self):
        num = self.num
        age = 0
        birthyear = int(num[0:2])
        currentyear = 2022
        if int(num[7]) == 1 or 2:
            age = currentyear - birthyear - 1900
        elif int(num[7]) == 3 or 4:
            age = currentyear - birthyear - 2000
        self.age = age

    def set_gen(self):
        num = self.num
        gen = ""
        if int(num[7]) == 1 or 3:
            gen = "남성"
        elif int(num[7]) == 2 or 4:
            gen = "여성"
        self.gen = gen

    def print(self):
        pass

    @staticmethod
    def new_person():
        return Person(input("이름 : "),
                      input("주민등록번호(000000-0000000) : "),
                      input("주소 : "))

    def __str__(self):
        return f"{self.name} {self.age} {self.gen} {self.addr}"

    @staticmethod
    def print_people(ls):
        for i in ls:
            print(i)

    @staticmethod
    def delete_person(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
