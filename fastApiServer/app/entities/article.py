from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.configs.database import Base
from sqlalchemy_utils import UUIDType
from app.entities.mixins import TimestampMixin


class Article(Base, TimestampMixin):

    __tablename__ = 'articles'

    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='articles')


    class Config:
        BaseConfig.arbitrary_types_allowed = True
        arbitrary_types_allowed = True

    def __str__(self):
        return f'글번호: {self.art_seq}, \n ' \
               f'이메일: {self.title}, \n ' \
               f'내용 {self.content} \n ' \
               f'아이디: {self.user_id} \n' \
               f'작성일: {self.create_at} \n' \
               f'수정일: {self.updated_at} \n'
