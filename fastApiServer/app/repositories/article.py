from app.database import engine, conn
from app.models.article import Article
import pymysql
from sqlalchemy.orm import sessionmaker, Session
pymysql.install_as_MySQLdb()


def find_articles_legacy():
    cursor = conn.cursor()
    sql = "select * from posts"
    cursor.execute(sql)
    return cursor.fetchall()


def find_articles(page: int, db: Session):
    return db.query(Article).all()
