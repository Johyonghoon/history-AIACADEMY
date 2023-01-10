import datetime

from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship


class Post(Base):

    __tablename__ = "posts"
    __table_args__ = {'extend_existing': True}

    post_id = Column(String(20), primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    create_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    class Config:
        arbitrary_types_allowed = True

