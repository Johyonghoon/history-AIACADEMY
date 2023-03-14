from faker import Faker
from fastapi.encoders import jsonable_encoder

from admin.utils import paging, between_random_date
from cruds.user import UserCrud
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, add_pagination, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse
from configs.database import get_db
from schemas.user import UserDTO, UserUpdate, UserList

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).add_user(request_user=dto)))


@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).login_user(request_user=dto)))


@router.post("/logout", status_code=200)
async def logout_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).logout_user(request_user=dto)))


@router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify")
async def modify_user(dto: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/reset-password")
async def reset_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(msg=UserCrud(db).reset_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.delete("/delete", tags=['delete'])
async def delete_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(msg=UserCrud(db).delete_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.get("/page/{page}", response_model=Page[UserList])
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    results = UserCrud(db).find_all_users_order_by_created_at()
    default_size = 5
    page_result = paginate(results, Params(page=page, size=default_size))
    count = UserCrud(db).count_all_users()
    pager = paging(request_page=page, row_cnt=count)
    return JSONResponse(status_code=200,
                        content=jsonable_encoder({
                            "pager": pager,
                            "users": page_result
                        }))


@router.get("/page/{page}/size/{size}", response_model=Page[UserList])
async def get_users_change_size(page: int, size: int, db: Session = Depends(get_db)):
    results = UserCrud(db).find_all_users_order_by_created_at()
    page_result = paginate(results, Params(page=page, size=size))
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(page_result))


@router.get("/job/{search}/{page}")
async def get_users_by_job(search: str, page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(UserCrud(db).find_users_by_job(search, page, db)))


@router.get("/dummy")
def insert_hunnit_dummy(db: Session = Depends(get_db)):
    faker = Faker('ko_KR')

    [UserCrud(db).add_user(UserDTO(
        user_email=faker.email(),
        password="qwer1234",
        user_name=faker.name(),
        birth=between_random_date(),
        address=faker.city())) for i in range(100)]


add_pagination(router)
