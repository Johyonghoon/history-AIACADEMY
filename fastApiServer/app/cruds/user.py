from abc import ABC
from typing import List

from app.admin.security import verify_password
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO
from sqlalchemy.orm import Session
import pymysql
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
        target = self.find_user_by_id(request_user)
        verified = verify_password(plain_password=request_user.password,
                                   hashed_password=target.password)
        print(f" 로그인 검증 결과: {verified}")
        if verified:
            return target
        else:
            return None

    def update_user(self, request_user: UserDTO) -> str:
        pass

    def delete_user(self, request_user: UserDTO) -> str:
        pass

    def find_all_users(self, page: int) -> List[User]:
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> UserDTO:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).first()

    def find_user_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        print(f" ###### user는 나오ㅑㅏㅆ엇는데 {user}")
        db_user = self.db.query(User).filter(User.user_email == user.user_email).first()
        print(f" ###### db_user {db_user}")
        if db_user is not None:
            print(f" ### db_user is not None 검증 {db_user.user_id}")
            return db_user.user_id
        else:
            print(f" ### db_user 안먹나?")
            return ""

