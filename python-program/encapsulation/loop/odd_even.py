from random_list import RandomList


class Oddeven(object):

    def __init__(self) -> None:
        pass

    def print(self):
        rl = RandomList()
        print([f"짝수 : {i}" if i % 2 == 0 else f"홀수 : {i}" for i in rl.get_random(10, 100, 10)])

    @staticmethod
    def main():
        oe = Oddeven()
        oe.print()


Oddeven.main()
