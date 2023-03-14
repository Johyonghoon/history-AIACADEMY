from abc import ABC
from typing import List

from admin.security import verify_password, generate_token, get_hashed_password, myuuid
from bases.user import UserBase
from entities.user import User
from schemas.user import UserDTO, UserUpdate
from sqlalchemy.orm import Session
import pymysql
from fastapi_pagination import Page, paginate, add_pagination
pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        user_id = self.find_user_id_by_email(request_user=request_user)
        if user_id == "":
            user.password = get_hashed_password(user.password)
            user.user_id = myuuid()
            is_success = self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            message = "SUCCESS: 회원가입이 완료되었습니다." \
                if is_success != 0 else "FAILURE: 비정상적인 이유로 회원가입이 실패하였습니다."
        else:
            message = "FAILURE: 이메일이 이미 존재합니다."
        return message

    def login_user(self, request_user: UserDTO) -> str:
        user_id = self.find_user_id_by_email(request_user=request_user)
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
                print("verified 실패")
                return "FAILURE: 비밀번호가 일치하지 않습니다."
        else:
            return "FAILURE: 이메일 주소가 존재하지 않습니다."

    def update_user(self, request_user: UserUpdate) -> str:
        db_user = self.find_user_by_id_for_update(request_user)
        print(f" ##### db_user을 확인해보자 {db_user}")
        for var, value in vars(request_user).items():
            setattr(db_user, var, value) if value else None
        is_success = self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return "SUCCESS" if is_success != 0 else "FAILED"

    def update_token(self, db_user: User, new_token: str):
        is_success = self.db.query(User).filter(User.user_id == db_user.user_id)\
            .update({User.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_user)
        return "SUCCESS" if is_success != 0 else "FAILED"

    def reset_password(self, request_user: UserDTO):
        user = User(**request_user.dict())
        user.password = get_hashed_password(user.password)
        is_success = self.db.query(User).filter(User.user_id == user.user_id)\
            .update({User.password: user.password}, synchronize_session=False)
        self.db.commit()
        # self.db.refresh(user)
        return "SUCCESS" if is_success != 0 else "FAILED"

    def delete_user(self, request_user: UserDTO) -> str:
        user = self.find_user_by_id(request_user)
        is_success = self.db.query(User).filter(User.user_id == user.user_id)\
            .delete(synchronize_session=False)
        self.db.commit()
        return "탈퇴 성공입니다" if is_success != 0 else "탈퇴 실패입니다."

    def find_all_users_order_by_created_at(self) -> List[User]:
        return self.db.query(User).order_by(User.created_at).all()

    def find_user_by_token(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.token == user.token).one_or_none()

    def match_token(self, request_user: UserDTO) -> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        print(f" ###### match_token 확인 {db_user}")
        return True if db_user != None else False

    def find_user_by_id(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).one_or_none()

    def count_all_users(self) -> int:
        return self.db.query(User).count()

    def logout_user(self, request_user: UserDTO) -> str:
        user = self.find_user_by_token(request_user)
        is_success = self.db.query(User).filter(User.user_id == user.user_id) \
            .update({User.token: ""}, synchronize_session=False)
        self.db.commit()
        print(f"토큰 삭제되면 1 리턴 예상함 : {is_success}")
        return "LOGOUT"

    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).one_or_none()

    def find_user_id_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.user_email == user.user_email).one_or_none()
        if db_user is not None:
            return db_user.user_id
        else:
            return ""

    def find_all_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

