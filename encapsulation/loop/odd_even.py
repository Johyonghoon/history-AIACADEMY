import random
from random_list import RandomList

class Oddeven(object):
    def __init__(self) -> None:
        pass

    def print(self):
        rl = RandomList()
        print(rl.get_random(2,10,1))

    @staticmethod
    def main():
        oe = Oddeven()
        oe.print()

Oddeven.main()