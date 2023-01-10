import datetime

from sqlalchemy.dialects.postgresql import UUID

from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship


class Article(Base, TimestampMixin):

    __tablename__ = "articles"
    __table_args__ = {'extend_existing': True}

    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='articles')

    class Config:
        arbitrary_types_allowed = True

