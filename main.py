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


class LoanUpdate(BaseModel):
    borrower: str
    item: str
    amount: int
    loan_date: str
    is_returned: bool


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


@app.put("/loans/{loan_id}")
def update_loan(loan_id: int, updated_loan: LoanUpdate):

    for index, loan in enumerate(loans):

        if loan["id"] == loan_id:

            loans[index] = {"id": loan_id, **updated_loan.model_dump()}

            return {"message": "修改借款紀錄成功", "data": loans[index]}

    raise HTTPException(status_code=404, detail="找不到這筆借款紀錄")


@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int):
    for index, loan in enumerate(loans):
        if loan["id"] == loan_id:
            deleted_loan = loans.pop(index)

            return {"message": "刪除借款紀錄成功", "data": deleted_loan}

    raise HTTPException(status_code=404, detail="找不到這筆借款紀錄")
