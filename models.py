from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    borrower: Mapped[str] = mapped_column(String(100))

    item: Mapped[str] = mapped_column(String(200))

    amount: Mapped[int] = mapped_column(Integer)

    loan_date: Mapped[str] = mapped_column(String(20))

    is_returned: Mapped[bool] = mapped_column(Boolean, default=False)
