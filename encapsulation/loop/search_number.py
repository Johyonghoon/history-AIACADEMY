"""
두자리 정수 랜덤 숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오.
예) [12, 23, 48, ..., ]
사용자의 input값이 12인 경우
출력값이 12, 48만 되도록 한다.
"""


from random_list import RandomList


class Searchnumber(object):
    def __init__(self) -> None:
        pass

    def print(self):
        rl = RandomList()
        j = list(rl.get_random(10, 100, 10))
        k = []
        print(j)
        for i in j:
            if i % 12 == 0:
                print(i)
            else:
                k.append(i)
                if len(k) == 10:
                    print("12의 배수가 없습니다.")

    @staticmethod
    def main():
        sn = Searchnumber()
        sn.print()


Searchnumber.main()
