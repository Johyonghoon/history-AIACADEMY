import os
import platform
myos = platform.system()
root_local = r"C:\Users\Quiet\PycharmProjects\MSAProject\fastApiServer"
root_docker = r"app"
root = root_local


def dir_path(param):
    if \
            (param == "admin") \
            or (param == "api") \
            or (param == "bases") \
            or (param == "configs") \
            or (param == "cruds") \
            or (param == "entities") \
            or (param == "models") \
            or (param == "routers") \
            or (param == "schemas") \
            or (param == "services") \
            or (param == "templates") \
            or (param == "tests") \
            or (param == "trains") \
            or (param == "utils"):
        return os.path.join(root, "app", param)


if __name__ == '__main__':
    print(">> "+dir_path("admin"))
