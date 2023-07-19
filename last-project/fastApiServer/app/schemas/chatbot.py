from typing import Optional
from pydantic import BaseModel


class UserVO(BaseModel):
    class Config:
        orm_mode = True


class ChatbotDTO(UserVO):
    question: Optional[str]
