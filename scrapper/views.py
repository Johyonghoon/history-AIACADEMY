from scrapper.domains import BugsMusic, Melon


class ScrapperController(object):

    @staticmethod
    def menu_1_bugsMusic(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2_melon(arg):
        melon = Melon(arg)
        melon.scrap()

