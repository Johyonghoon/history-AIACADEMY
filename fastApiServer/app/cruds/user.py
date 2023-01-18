from abc import ABC
from typing import List

from app.admin.security import verify_password, generate_token
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
        user_id = self.find_user_by_email(request_user=request_user)
        if user_id != "":
            request_user.user_id = user_id
            db_user = self.find_user_by_id(request_user)
            verified = verify_password(plain_password=request_user.password,
                                       hashed_password=db_user.password)
            if verified:
                new_token = generate_token(request_user.user_email)
                request_user.token = new_token
                self.update_token(db_user, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다."
        else:
            return "FAILURE: 이메일 주소가 존재하지 않습니다."

    def update_user(self, request_user: UserDTO) -> str:
        pass

    def update_token(self, db_user: User, new_token: str):
        is_success = self.db.query(User).filter(User.user_id == db_user.user_id)\
            .update({User.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_user)
        return is_success

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
        db_user = self.db.query(User).filter(User.user_email == user.user_email).first()
        if db_user is not None:
            return db_user.user_id
        else:
            return ""


