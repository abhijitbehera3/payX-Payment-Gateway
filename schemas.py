from pydantic import BaseModel, EmailStr, Field
from typing import Literal


class Customer(BaseModel):

    email: EmailStr

    phone: str


class TransactionRequest(BaseModel):

    amount: float = Field(
        gt=0
    )

    currency: Literal["INR"]

    payment_method: Literal[
        "upi",
        "credit_card",
        "debit_card",
        "net_banking"
    ]

    reference_id: str

    customer: Customer


class TransactionData(BaseModel):

    transaction_id: str

    status: str

    amount: float

    currency: str


class TransactionResponse(BaseModel):

    success: bool

    data: TransactionData

    metadata: dict