import random

class Bubble(object):
    def __init__(self) -> None:
        pass

    def extract_random(self):
        return random.sample(range(1, 100), k=10)

    def print_bubble(self):
        a = self.extract_random()
        for i in a:
            if i % 2 == 1:
                print(i)

    @staticmethod
    def main():
        bubble = Bubble()
        
        bubble.print_bubble()

Bubble.main()