from abc import ABC
from typing import List

from sqlalchemy import select

from app.bases.user import UserBase
from app.database import conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import Session

from app.schemas.user import UserDTO

pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        self.db.add(user)
        self.db.commit()
        return "success"

    def login(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        print(f" email {user.user_email}")

    def update_user(self, request_user: UserDTO) -> str:
        pass

    def delete_user(self, request_user: UserDTO) -> str:
        pass

    def find_all_users(self, page: int) -> List[User]:
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> UserDTO:
        pass

    def find_user_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.user_email == user.user_email).first()
        if db_user is not None:
            return db_user.user_id
        else:
            return ""

