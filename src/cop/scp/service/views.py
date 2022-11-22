from src.cop.scp.service.services import BugsMusic, Melon


class ScrapperController(object):

    @staticmethod
    def menu_1_bugsMusic(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2_melon(arg):
        Melon(arg)

