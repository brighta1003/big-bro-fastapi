from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="大哥來算帳 API",
    description="借款與還款紀錄管理 API",
    version="1.0.0",
)


class LoanCreate(BaseModel):
    borrower: str
    item: str
    amount: int
    loan_date: str
    is_returned: bool = False


loans = []
next_id = 1


@app.get("/")
def root():
    return {"message": "大哥來算帳 API 運作中"}


@app.get("/loans")
def get_loans():
    return {"data": loans}


@app.get("/loans/{loan_id}")
def get_loan(loan_id: int):
    for loan in loans:
        if loan["id"] == loan_id:
            return {"data": loan}

    raise HTTPException(status_code=404, detail="找不到這筆借貸紀錄")


@app.post("/loans")
def create_loan(loan: LoanCreate):
    global next_id

    new_loan = {"id": next_id, **loan.model_dump()}

    loans.append(new_loan)
    next_id += 1

    return {"message": "新增借款紀錄成功", "data": new_loan}
