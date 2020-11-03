import os
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
            "Message": "API is up and running",
            "DATABASE": [os.getenv("DATABASE_URL"), os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PASSWORD")],
            "AUTHENTICATION": os.getenv("AUTHENTICATION")
           }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}