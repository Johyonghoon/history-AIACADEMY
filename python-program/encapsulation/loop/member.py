"""
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
"""


class Member(object):

    def __init__(self, account, pw, name):
        self.account = account
        self.pw = pw
        self.name = name

    def print(self):
        print("ID PASSWORD NAME")
        print(f'{self.account} {self.pw} {self.name}')

    @staticmethod
    def print_menu():
        print("1. 수강생 등록")
        print("2. 수강생 목록")
        print("3. 수강생 삭제")
        print("4. 종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def new_member():
        account = input("account : ")
        pw = input("Password : ")
        name = input("이름 : ")
        return Member(account, pw, name)

    def print_info(self):
        print(f"{self.account} {self.pw} {self.name}")

    @staticmethod
    def all_members(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def delete_member(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("### 수강생 등록 ###")
                ls.append(Member.new_member())
            elif menu == 2:
                print("### 수강생 목록 ###")
                Member.all_members(ls)
            elif menu == 3:
                print("### 수강생 삭제 ###")
                Member.delete_member(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("### 종료 ###")
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")


Member.main()
