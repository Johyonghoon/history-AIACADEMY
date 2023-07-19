from abc import abstractmethod, ABCMeta
from typing import List
from entities.user import User
from schemas.user import UserDTO


class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def login_user(self, request_user: UserDTO) -> User: pass

    @abstractmethod
    def logout_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def update_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def reset_password(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def delete_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def find_all_users_order_by_created_at(self, request_user: UserDTO) -> List[User]: pass

    @abstractmethod
    def find_all_users(self, page: int) -> List[User]: pass

    @abstractmethod
    def find_user_by_id(self, request_user: UserDTO) -> UserDTO: pass

    @abstractmethod
    def find_user_id_by_email(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def match_token(self, request_user: UserDTO) -> bool: pass

    @abstractmethod
    def count_all_users(self) -> int: pass