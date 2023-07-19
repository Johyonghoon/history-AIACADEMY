"""
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장가능합니다.
"""


class Contacts(object):

    def __init__(self, name, pnum, mail, addr):
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr

    def print(self):
        pass

    @staticmethod
    def new_contact():
        return Contacts(input("이름"),
                        input("전화번호"),
                        input("이메일"),
                        input("주소"))

    def __str__(self):
        return f"{self.name} {self.pnum} {self.mail} {self.addr}"

    @staticmethod
    def print_contacts(ls):
        for i in ls:
            print(i)

    @staticmethod
    def delete_contact(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
