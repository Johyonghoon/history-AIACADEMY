from src.uss.mpe.service.bmi import Bmi
from src.uss.mpe.service.contacts import Contacts
from src.uss.mpe.service.grade import Grade
from src.uss.mpe.service.person import Person
from src.cmm.service.menu import Menu


ls = []
while True:
    menu = Menu.menu(["종료", "BMI", "연락처", "성적표", "자기소개"])
    if menu == 0:
        print("### 전체메뉴 종료 ###")
        break
    elif menu == 1:
        print("### BMI ###")
        print("*" * 40)
        submenu = Menu.menu(["BMI 종료", "BMI 등록", "BMI 목록", "BMI 삭제"])
        if submenu == 0:
            print("### BMI 종료 ###")
            break
        elif submenu == 1:
            print("### BMI 등록 ###")
            sub_bmi = Bmi.new_condi()
            ls.append(sub_bmi)
        elif submenu == 2:
            print("### BMI 목록 ###")
            Bmi.print_condis(ls)
        elif submenu == 3:
            print("### BMI 삭제 ###")
            Bmi.delete_condi(ls, input("삭제할 이름 : "))
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
    elif menu == 2:
        print("### 연락처 ###")
        print("*" * 40)
        submenu = Menu.menu(["연락처 종료", "연락처 등록", "연락처 목록", "연락처 삭제"])
        if submenu == 0:
            print("### 연락처 종료 ###")
            break
        elif submenu == 1:
            print("### 연락처 등록 ###")
            sub_contact = Contacts.new_contact()
            ls.append(sub_contact)
        elif submenu == 2:
            print("### 연락처 목록 ###")
            Contacts.print_contacts(ls)
        elif submenu == 3:
            print("### 연락처 삭제 ###")
            Contacts.delete_contact(ls, input("삭제할 이름을 입력하세요. "))
        else:
            print("잘못된 숫자입니다. 다시 입력하세요.")
    elif menu == 3:
        print("### 성적표 ###")
        print("*" * 40)
        submenu = Menu.menu(["성적표 등록", "성적표 목록", "성적표 삭제", "성적표 종료"])
        if submenu == 0:
            print("### 성적표 종료 ###")
            break
        elif submenu == 1:
            print("### 성적표 등록 ###")
            sub_grade = Grade.new_grade()
            ls.append(sub_grade)
        elif submenu == 2:
            print("### 성적표 목록 ###")
            Grade.print_grades(ls)
        elif submenu == 3:
            print("### 성적표 삭제 ###")
            Grade.delete_grade(ls, input("삭제할 이름을 입력하세요. "))
        else:
            print("잘못된 숫자입니다. 다시 입력하세요.")
    elif menu == 4:
        print("### 자기소개 ###")
        print("*" * 40)
        submenu = Menu.menu(["### 자기소개 등록 ###", "### 자기소개 목록 ###", "### 자기소개 삭제 ###", "### 자기소개 종료 ###"])
        if submenu == 0:
            print("### 자기소개 종료 ###")
            break
        elif submenu == 1:
            print("### 자기소개 등록 ###")
            sub_person = Person.new_person()
            ls.append(sub_person)
        elif submenu == 2:
            print("### 자기소개 목록 ###")
            Person.print_people(ls)
        elif submenu == 3:
            print("### 자기소개 삭제 ###")
            Person.delete_person(ls, input("삭제할 이름을 입력하세요. "))
        else:
            print("잘못된 숫자입니다. 다시 입력하세요.")
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
