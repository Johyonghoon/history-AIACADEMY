from src.dam.per.bicycle.models import BicycleModel


class BicycleController(object):

    model = BicycleModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴 선택 : ')


if __name__ == "__main__":
    api = BicycleController()
    while True:
        menu = my_menu(["종료", "시각화", "모델링", "머신 러닝", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            a = BicycleModel()
            b = a.new_model("train.csv")
            print(f"Train type : {type(b)}")
            print(f"Train columns : {b.columns}")
            print(f"Train head : {b.head()}")
            print(f"Train null 개수 : \n{b.isnull().sum()}")
            # ['id', 'hour', 'hour_bef_temperature', 'hour_bef_precipitation',
            #        'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
            #        'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count']
            # Train null 개수
            # hour_bef_temperature 2
            # hour_bef_precipitation 2
            # hour_bef_windspeed 9
            # hour_bef_humidity 2
            # hour_bef_visibility 2
            # hour_bef_ozone 76
            # hour_bef_pm10 90
            # hour_bef_pm2.5 117
        elif menu == "2":
            print(" ### 모델링 ### ")
        elif menu == "3":
            print(" ### 머신 러닝 ### ")
        elif menu == "4":
            print(" ### 배포 ### ")
        else:
            print("다른 메뉴를 선택하세요.")
