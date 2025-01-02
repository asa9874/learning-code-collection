from fastapi import FastAPI
from enum import Enum

#FastAPI 인스턴스 생성 
app = FastAPI()

#경로 작동 데코레이터
@app.get("/")
async def root():#엔드포인트
    return {"message": "Hello World"} #응답



#경로 매개변수
@app.get("/items/{item_id}")# /items/1 -> item_id = 1
async def getItemById(item_id: int): #경로 매개변수 item_id
    return {"item_Id": item_id}



#열거형 클래스
class HumanId(int, Enum): #열거형 클래스
    me=1
    you=2
    we=3


#사전 정의된 값으로 경로 매개변수 사용
@app.get("/humans/{human_id}")
async def getHumanById(human_id: HumanId):
    if human_id == HumanId.me:
        return {"human_id": human_id, "message": "I am"}
    elif human_id == HumanId.you:
        return {"human_id": human_id, "message": "You are"}
    else:
        return {"human_id": human_id, "message": "We are"}


#경로 매개변수와 쿼리 매개변수
@app.get("/test")
async def test(id: int,name: str=None):
    return {"name": name, "id": id}