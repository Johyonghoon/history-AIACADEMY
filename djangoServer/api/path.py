import os
import platform
myos = platform.system()
root = r"C:\Users\Quiet\PycharmProjects\MSAProject\djangoServer"


def dir_path(param):
    if \
            param == "algorithms":
        return os.path.join(root, "exrc", param)
    elif \
            (param == "exrc_posts") \
            or (param == "exrc_users")\
            or (param == "login"):
        return os.path.join(root, "exrc", "auth", param)
    elif \
            (param == "fashion") \
            or (param == "fruits") \
            or (param == "iris") \
            or (param == "mnist") \
            or (param == "aitrader"):
        return os.path.join(root, "exrc", "dlearn", param)
    elif \
            (param == "imdb") \
            or (param == "samsung_report"):
        return os.path.join(root, "exrc", "nlp", param)
    elif \
            param == "stroke":
        return os.path.join(root, "exrc", param)
    elif \
            param == "webcrawler":
        return os.path.join(root, "exrc", param)
    elif \
            param == "naver_movie":
        return os.path.join(root, "exrc", "webcrawler", param)
    elif \
            (param == "blog_users") \
            or (param == "comments")\
            or (param == "posts")\
            or (param == "tags")\
            or (param == "views"):
        return os.path.join(root, "blog", param)
    elif \
            (param == "cinemas") \
            or (param == "movie_users") \
            or (param == "movies") \
            or (param == "showtimes") \
            or (param == "theater_tickets") \
            or (param == "theaters"):
        return os.path.join(root, "movie", param)
    elif \
            (param == "carts") \
            or (param == "categories") \
            or (param == "deliveries") \
            or (param == "orders") \
            or (param == "products") \
            or (param == "shop_users"):
        return os.path.join(root, "shop", param)
    elif \
            param == "users":
        return os.path.join(root, param)


if __name__ == '__main__':
    print(">> "+dir_path("carts"))
