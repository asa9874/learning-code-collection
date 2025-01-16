from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn

app = FastAPI()

# 클라이언트를 관리하는 클래스
class ConnectionManager:
    def __init__(self):
        # 활성화된 웹소켓 연결을 저장하는 리스트
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        # 웹소켓 연결을 수락하고 리스트에 추가
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        # 웹소켓 연결을 리스트에서 제거
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        # 특정 클라이언트에게 메시지를 전송
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        # 연결된 모든 클라이언트에게 메시지를 전송
        for connection in self.active_connections:
            await connection.send_text(message)

# ConnectionManager 인스턴스를 생성
manager = ConnectionManager()

# 웹소켓 엔드포인트 정의
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    # 새로운 클라이언트 연결을 관리하고, 연결 메시지를 브로드캐스트
    await manager.connect(websocket)
    await manager.broadcast(f"{client_id}님이 채팅에 참여했습니다.")
    try:
        while True:
            # 클라이언트로부터 메시지를 수신하고, 모든 클라이언트에게 브로드캐스트
            data = await websocket.receive_text()
            await manager.broadcast(f"{client_id}: {data}")
    except WebSocketDisconnect:
        # 클라이언트 연결이 끊어지면 관리에서 제거하고, 연결 해제 메시지를 브로드캐스트
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id}님이 채팅을 떠났습니다")

# 직접 실행 가능하도록 설정
if __name__ == "__main__":
    uvicorn.run(
        "websocket:app",  # "파일이름:FastAPI 객체 이름"
        host="127.0.0.1",  # 로컬에서 실행 (외부 접근 시 "0.0.0.0" 사용 가능)
        port=8000,  # 서버가 실행될 포트 번호
        reload=True  # 코드 변경 시 서버 자동 재시작 (개발 모드에서 유용)
    )
