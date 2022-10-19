import random

class Bubble(object):
    def __init__(self) -> None:
        pass

    def extract_random(self):
        return random.sample(range(1, 100), k=10)

    def print_bubble(self):
        for i in self.extract_random():
            print(i)

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.extract_random()
        bubble.print_bubble()

Bubble.main()
