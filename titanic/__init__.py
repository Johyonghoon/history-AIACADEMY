from titanic.template import Plot
from titanic.views import TitanicController
from util.menu import Menu

if __name__ == "__main__":
    api = TitanicController()
    while True:
        menu = Menu.menu(["종료", "시각화", "모델링", "머신 러닝", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_sex()
        elif menu == "2":
            print(" ### 모델링 ### ")
        elif menu == "3":
            print(" ### 머신 러닝 ### ")
        elif menu == "4":
            print(" ### 배포 ### ")
        else:
            print("다른 메뉴를 선택하세요.")
