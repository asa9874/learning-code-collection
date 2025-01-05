from enum import Enum
from typing import Annotated, Literal,Union
from fastapi import FastAPI, Query, Path, Cookie, Response
from pydantic import BaseModel, Field
import uvicorn

 #FastAPI 인스턴스 생성 
app = FastAPI()

#경로 작동 데코레이터
@app.get("/")
async def root():#엔드포인트
    return {"message": "Hello World"} #응답



#0. 경로 매개변수
##경로 매개변수는 경로의 일부로 전달되는 매개변수
@app.get("/items/{item_id}")# /items/1 -> item_id = 1
async def getItemById(item_id: int): #경로 매개변수 item_id
    return {"item_Id": item_id}



#1. 사전 정의된 값으로 경로 매개변수 사용
## 열거형 클래스
class HumanId(int, Enum): #열거형 클래스
    me=1
    you=2
    we=3


## 열거형 클래스를 사용하여 사전 정의된 값으로 경로 매개변수 사용
@app.get("/humans/{human_id}")
async def getHumanById(human_id: HumanId):
    if human_id == HumanId.me:
        return {"human_id": human_id, "message": "I am"}
    elif human_id == HumanId.you:
        return {"human_id": human_id, "message": "You are"}
    else:
        return {"human_id": human_id, "message": "We are"}



#2. 경로 매개변수와 쿼리 매개변수
## 경로 매개변수와 쿼리 매개변수를 동시에 사용
@app.get("/test")
async def test(id: int,name: str=None):
    return {"name": name, "id": id}




#3. 쿼리 매개변수
## 데이터 모델 정의
class Book(BaseModel):
    title: str
    author: str
    price: float
    is_available: bool = True  # 기본값 설정

## POST 요청 처리
@app.post("/books/")
async def create_book(book: Book):
    return {"message": "Book created successfully", "book": book}





#4. 쿼리 매개변수 검증 Query
## Query 클래스를 사용하여 쿼리 매개변수 유효성 검사
@app.get("/items2/")
async def get_item2(name: str, price: float, limit: int = Query(..., ge=1, le=10)):
    return {"name": name, "price": price, "limit": limit}

## 여러 쿼리 매개변수 유효성 검사
@app.get("/items3/")
async def get_item3(q: Union[str, None] = Query(...), limit: int = Query(..., ge=1, le=10)):
    return {"search_query": q, "limit": limit,"search_Id": q}



#5. 경로 매개변수 유효성 검사
@app.get("/items4/{item_id}")
async def get_item4(
    item_id: int = Path(..., ge=1, le=100)
):
    return {"item_id": item_id}




#6. Field
class PaginationParams(BaseModel):
    page: int = Field(1, ge=1)
    size: int = Field(10, gt=0, le=100)
    sort_by: Literal["name", "date", "price"] = "date"
    filter: str = Field("", max_length=50)

@app.get("/products/")
async def read_products(pagination: Annotated[PaginationParams, Query()]):
    return pagination


# 7. 쿠키
@app.get("/setcookie")
def set_cookie(response: Response):
    response.set_cookie(key="my_cookie", value="cookie_value", httponly=True, max_age=3600)
    return {"message": "쿠키가 설정되었습니다!"}


# 직접 실행 가능하도록 설정
if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # "파일이름:FastAPI 객체 이름"
        host="127.0.0.1",  # 또는 "0.0.0.0" (외부에서 접근 가능)
        port=8000,  # 원하는 포트 번호
        reload=True  # 개발 모드에서 코드 변경 시 자동 재시작
    )