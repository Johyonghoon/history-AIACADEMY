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


time_string = input()

if Time.is_date_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')