import uuid

from sqlalchemy.dialects.postgresql import UUID

from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship


class User(Base, TimestampMixin):

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20))
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True
