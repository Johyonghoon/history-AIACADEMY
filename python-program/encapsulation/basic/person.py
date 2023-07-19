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
    def __init__(self, name, num, add) -> None:
        self.name = name
        self.num = num
        self.add = add
        self.age = 0
        self.gen = ""

    def set_age(self):
        
        num = self.num
        age = self.age
        birthyear = int(num[0]) * 10 + int(num[1])
        todayyear = 122
        if int(num[6]) == 1 or 2 or 5 or 6:
            age = todayyear - birthyear
        elif int(num[6]) == 3 or 4 or 7 or 8: 
            age = todayyear - birthyear - 100
        self.age = age

    def set_gen(self):
        
        num = self.num
        k = int(num[6])
        if k == 1 or 3:
            gen = "남성"
        elif k == 2 or 4:
            gen = "여성"
        elif k == 5 or 7:
            gen = "외국인 남성"
        elif k == 6 or 8:
            gen = "외국인 여성"
        else:
            gen = "잘못된 주민번호입니다."
        self.gen = gen

    def print_age(self):
        name = self.name
  
        add = self.add
        print("### 자기소개어플 ###")
        print("*" * 40)
        print("이름 : " f'{name}')
        print("나이 : " f'{self.age}')
        print("성별 : " f'{self.gen}')
        print("주소 : " f'{add}')
        print("*" * 40)

    @staticmethod
    def main():
        name = input("이름: ")
        num = input("주민번호: ")
        add = input("주소 : ")
        person = Person(name, num, add)
        person.set_age()
        person.set_gen()
        person.print_age()


Person.main()
