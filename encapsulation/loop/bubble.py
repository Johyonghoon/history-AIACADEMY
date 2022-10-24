from random_list import RandomList


class Bubble(object):
    def __init__(self) -> None:
        pass

    # noinspection PyMethodMayBeStatic
    def print_bubble(self):
        rl = RandomList()
        ls = rl.get_random(start=10, end=100, count=10)
        print(ls)
        for i in range(len(ls)-1):
            for j in range(len(ls)-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
        print("*"*40)
        print(ls)

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print_bubble()


Bubble.main()
