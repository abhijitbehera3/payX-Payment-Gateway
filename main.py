from fastapi import FastAPI

from .database import Base, engine
from . import models

from .routers.transactions import router as transaction_router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="payX Payment Gateway",
    version="1.0.0"
)


app.include_router(
    transaction_router
)


@app.get("/")
def home():

    return {
        "message": "payX Payment Gateway API",
        "status": "running"
    }