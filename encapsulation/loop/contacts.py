'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장가능합니다.
'''
class Contact(object):
    def __init__(self, name, tel, mail, add) -> None:
        self.name = name
        self.tel = tel
        self.mail = mail
        self.add = add

    def print(self):
        print("이름 전화번호, 이메일, 주소")
        print("*"*50)
        print(f'{self.name} {self.tel} {self.mail} {self.add}')

    @staticmethod
    def new_contact():
        name = input("이름 : ")
        tel = input("전화번호 : ")
        mail = input("이메일 : ")
        add = input("주소 : ")
        return Contact(name, tel, mail, add)

    def print_info(self):
        print(f'{self.name}{self.tel}{self.mail}{self.add}')

    @staticmethod
    def print_contacts(ls):
        for i in ls:
            i.print_info()
        
    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 목록")
        print("3. 연락처 삭제")
        print("4. 종료")
        return int(input("메뉴 선택 :"))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print("### 연락처 등록 ###")
                contact = Contact.new_contact()
                ls.append(contact)
            elif menu == 2:
                print("### 연락처 목록 ###")
                Contact.print_contacts(ls)
            elif menu == 3:
                print("### 연락처 삭제 ###")
            elif menu == 4:
                print("주소록 어플을 종료합니다.")
                break

Contact.main()
