class Date:

    @staticmethod
    def is_date_valid(date):
        year, month, day = map(int, date.split('-'))
        return month <= 12 and day <= 31


class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, hour, minute, second):
        cls.hour = hour
        cls.minute = minute
        cls.second = second
        return hour, minute, second

    def is_date_valid(self, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        self.from_string(hour, minute, second)
        return hour <= 24 and minute <= 60 and second <= 60


if __name__ == '__main__':
    while True:
        menu = input("메뉴 입력 : ")
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("### 연습문제 : 날짜 클래스 만들기 ###")
            if Date.is_date_valid('2000-10-31'):
                print('올바른 날짜 형식입니다.')
            else:
                print('잘못된 날짜 형식입니다.')
        elif menu == '2':
            print("### 심사문제 : 시간 클래스 만들기 ###")
            print("시:분:초 형식으로 시간을 입력하세요. ")
            time_string = input()

            if Time.is_date_valid(time_string):
                t = Time.from_string(time_string)
                print(t.hour, t.minute, t.second)
            else:
                print('잘못된 시간 형식입니다.')



