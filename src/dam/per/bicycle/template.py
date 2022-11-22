from src.dam.per.bicycle.models import BicycleModel
from src.cmm.service.dataset import Dataset


class Template(object):
    dataset = Dataset()
    model = BicycleModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

