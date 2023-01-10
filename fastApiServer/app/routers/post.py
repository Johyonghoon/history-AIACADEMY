from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
import app.repositories.post as dao
router = APIRouter()


@router.get("/{page}")
async def get_posts(page: int, db: Session = Depends(get_db)):
    ls = dao.find_posts(page, db)
    return {"data": ls}
