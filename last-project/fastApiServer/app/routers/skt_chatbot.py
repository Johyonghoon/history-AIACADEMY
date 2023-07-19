from fastapi import APIRouter
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from app.services.chatbot.kakao_gpt3 import KakaoGpt3
from app.tests.find_answer_test import FindAnswerTest

router = APIRouter()
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello WebSocket</title>
    <link href="<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<style>
body {
    background-color: #f5f5f5;
}
#main-content {
    max-width: 940px;
    padding: 2em 3em;
    margin: 0 auto 20px;
    background-color: #fff;
    border: 1px solid #e5e5e5;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
}
</style>
</head>
<body>
<h4 style="color: #ff0000">채팅창</h4>
 <h2>Your ID: <span id="ws-id"></span></h2>
<div id="main-content" class="container">
    <div class="row">
        <div class="col-md-6">
            <form class="form-inline" onsubmit="sendMessage(event)">
                <div class="form-group">
                    <input type="text" id="messageText" autocomplete="off"/>
                    <button>Send</button>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
                    <h3>메세지</h3>
                <ul id="messages">
                </ul>
        </div>
    </div>
</div>
    <script>
        var client_id = Date.now()
        document.querySelector("#ws-id").textContent = client_id;
        var ws = new WebSocket(`ws://localhost:8000/skt-chatbot/foodbot`);
        ws.onmessage = function(event) {
            var messages = document.getElementById('messages')
            var message = document.createElement('li')
            var content = document.createTextNode(event.data)
            message.appendChild(content)
            messages.appendChild(message)
        };
        function sendMessage(event) {
            var input = document.getElementById("messageText")
            ws.send(input.value)
            input.value = ''
            event.preventDefault()
        }
    </script>
</body>
"""


@router.get("/")
async def get():
    return HTMLResponse(html)


# @router.websocket("/skt-gpt2")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         output = KakaoGpt3().classify_sentence(data)
#         await websocket.send_text(f"보낸 메세지: {data}")
#         await websocket.send_text(f"KoGPT2 챗봇의 답변: {output}")


@router.websocket("/kakao-gpt3")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        output = KakaoGpt3().chatting(data)
        await websocket.send_text(f"보낸 메세지: {data}")
        await websocket.send_text(f"카카오 챗봇의 답변: {output}")


@router.websocket("/foodbot")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        output = FindAnswerTest().process(data)
        await websocket.send_text(f"보낸 메세지: {data}")
        await websocket.send_text(f"카카오 챗봇의 답변: {output}")
