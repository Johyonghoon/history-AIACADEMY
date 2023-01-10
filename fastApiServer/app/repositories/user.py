from app.database import engine, conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import sessionmaker, Session
pymysql.install_as_MySQLdb()


def join(item, db):
    return None


def login(id, item, db):
    return None


def update(id, item, db):
    return None


def delete(id, item, db):
    return None


def find_users(page: int, db: Session):
    return db.query(User).all()


def find_user(id, db):
    return None


def find_users_by_job(search, page, db):
    return None


def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()
