import datetime
from typing import List

from pydantic import BaseModel


class Post(BaseModel):
    post_id: int
    title: str
    content: str
    create_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PostList(Post):
    posts: List[Post] = []
