from fastapi import FastAPI

app = FastAPI(
    title="大哥來算帳 API",
    description="借款與還款紀錄管理 API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "大哥來算帳 API 運作中"}
