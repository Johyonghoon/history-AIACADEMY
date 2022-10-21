'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
'''


class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name


    def print_info(self):
        print("ID PASSWORD NAME")
        print(f'{self.id} {self.pw} {self.name}')

    @staticmethod
    def print_menu():
        print("1. 수강생 등록")
        print("2. 수강생 목록")
        print("3. 수강생 삭제")
        print("4. 종료")
        return int(input("메뉴 선택"))

    @staticmethod
    def new_member():
        id = input("ID : ")
        pw = input("Password : ")
        name = input("이름 : ")
        return Member(id, pw, name)

    @staticmethod
    def all_members(ls):
        [i.print_info() for i in ls]


    @staticmethod
    def delete_member():
        pass

    @staticmethod
    def main():
        ls= []
        while True:
            menu = Member.print_menu()
            if menu == 1 :
                print("### 등록 ###")
                ls.append(Member.new_member())
            elif menu == 2 :
                print("### 목록 ###")
                Member.all_members(ls)
            elif menu == 3 :
                print("### 삭제 ###")
                Member.delete_member()
            elif menu == 4 :
                print("### 종료 ###")
                break
            else :
                print("잘못된 입력입니다. 다시 입력하세요.")

Member.main()