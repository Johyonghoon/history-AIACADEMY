from random_list import RandomList


class Oddeven(object):
    def __init__(self) -> None:
        pass

    def print(self):
        rl = RandomList()
        for i in rl.get_random(10,100,10):
            if i % 2 == 0:
                print(f"짝수 : {i}")
            else:
                print(f"홀수 : {i}")

    @staticmethod
    def main():
        oe = Oddeven()
        oe.print()

Oddeven.main()