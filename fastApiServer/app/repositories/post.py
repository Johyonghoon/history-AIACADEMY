from app.database import engine, conn
from app.models.post import Post
import pymysql
from sqlalchemy.orm import sessionmaker, Session
pymysql.install_as_MySQLdb()


def find_posts_legacy():
    cursor = conn.cursor()
    sql = "select * from posts"
    cursor.execute(sql)
    return cursor.fetchall()


def find_posts(db: Session):
    return db.query(Post).all()
