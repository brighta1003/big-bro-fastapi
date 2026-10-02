from fastapi import FastAPI

from database import engine, Base
import models
from sqlalchemy import text

app = FastAPI(
    title="大哥來算帳 API",
    description="借款與還款紀錄管理 API",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "大哥來算帳 API 運作中"}


@app.get("/db-test")
def db_test():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT VERSION()"))

        version = result.scalar()

    return {"database": version}
