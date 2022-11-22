class Menu(object):

    def __init__(self):
        pass

    @staticmethod
    def menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input("목록 선택 : ")

    @staticmethod
    def main():
        pass


Menu.main()
