USERNAME = "root"
PASSWORD = "root"
HOSTNAME = "host.docker.internal"  # "localhost"
DATABASE = "mydb"
PORT = 3306
CHARSET = "utf8mb4"
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"


def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

"""
DB_HOST = "127.0.0.1"
DB_USER = "homestead"
DB_PASSWORD = "secret"
DB_NAME = "homestead"
"""