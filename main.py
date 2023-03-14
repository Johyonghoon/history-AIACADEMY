import os
import sys
import logging

from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from admin.utils import current_time
from configs.env import DB_URL
from configs.database import init_db
from fastapi_pagination import add_pagination
from fastapi import FastAPI, APIRouter, Depends, HTTPException, WebSocket
from fastapi.security import APIKeyHeader

from routers.user import router as user_router
from mangum import Mangum

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")

print(f" ################ app.main Started At {current_time()} ################# ")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
app = FastAPI()
add_pagination(app)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@app.get("/")
async def home():
    return HTMLResponse(content=f"""
        <body>
        <div>
            <h1 style="width:400px;margin:50px auto">
                { current_time()} <br/>
                현재 서버 구동 중 입니다. 
             </h1>
        </div>
        </body>
            """)


@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/no-match-token")
async def no_match_token():
    return {"message": f"토큰 유효시간이 지났습니다."}
