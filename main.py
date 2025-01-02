from fastapi import FastAPI

#FastAPI 인스턴스 생성 
app = FastAPI()

#경로 작동 데코레이터
@app.get("/")
async def root():#엔드포인트
    return {"message": "Hello World"} #응답