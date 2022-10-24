import random


class RandomList(object):
    def __init__(self) -> None:
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start,end), k=count)

    def print(self):
        print(self.get_random(10, 100, 10))

    @staticmethod
    def main():
        randomList = RandomList()
        randomList.print()


RandomList.main()
