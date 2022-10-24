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
        print("이름 나이 성별 주소")
        print("*" * 40)
        print(f"{self.name} {self.age} {self.gen} {self.addr}")

    @staticmethod
    def print_menu():
        print("### 목록 ###")
        print("1. 개인정보 입력")
        print("2. 개인정보 목록")
        print("3. 개인정보 삭제")
        print("0. 종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def new_person():
        return Person(input("이름 : "),
                      input("주민등록번호(000000-0000000) : "),
                      input("주소 : "))

    def print_info(self):
        print(f"{self.name} {self.age} {self.gen} {self.addr}")

    @staticmethod
    def print_people(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def delete_person(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 1:
                print("### 개인정보 입력 ###")
                person = Person.new_person()
                ls.append(person)
            elif menu == 2:
                print("### 개인정보 목록 ###")
                print("이름 나이 성별 주소")
                print("*" * 40)
                Person.print_people(ls)
            elif menu == 3:
                print("### 개인정보 삭제 ###")
                Person.delete_person(ls, input("삭제할 이름: "))
            elif menu == 0:
                print("### 종료 ###")
                break


Person.main()
