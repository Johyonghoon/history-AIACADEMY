from starlette.responses import JSONResponse, HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, WebSocket, Request

from app.admin.utils import current_time
from app.schemas.chatbot import ChatbotDTO
from app.services.chatbot.kakao_gpt3 import KakaoGpt3

router = APIRouter()
# html파일을 서비스할 수 있는 jinja설정 (/templates 폴더사용)
templates = Jinja2Templates(directory="templates/")


@router.get("")
async def chatbot_home():
    return HTMLResponse(content=f"""
        <body>
        <div>
            <h1 style="width:400px;margin:50px auto">
                { current_time() } <br/>
                현재 서버 구동 중 입니다. 
             </h1>
        </div>
        </body>
            """)

@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 웹소켓 연결을 테스트 할 수 있는 웹페이지 (http://127.0.0.1:8000/client)
@router.get("/client", status_code=202)
async def client(request: Request):
    # /templates/client.html파일을 response함
    return templates.TemplateResponse("client.html", {"request":request})


# 웹소켓 설정 ws://127.0.0.1:8000/ws 로 접속할 수 있음
@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    print(f"client connected : {websocket.client}")
    await websocket.accept()  # client의 websocket접속 허용
    await websocket.send_text(f"Welcome client #{client_id} : {websocket.client}")
    while True:
        data = await websocket.receive_text()  # client 메시지 수신대기
        print(f"message received : {data} from : {websocket.client}")
        await websocket.send_text(f"Message text was: {data}")  # client에 메시지 전달


# kakao_gpt3 postman 확인 완료
@router.get("/answer", status_code=201)
async def answer_question(dto: ChatbotDTO):
    return JSONResponse(status_code=201,
                        content=dict(msg=KakaoGpt3().chatting(request_data=dto)))
