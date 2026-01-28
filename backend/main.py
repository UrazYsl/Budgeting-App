from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel

from database import SessionLocal
from crud import create_item, read_items

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    return {"ok": db.execute(text("select 1")).scalar_one() == 1}

@app.post("/items/")
def create_item_endpoint(item: Item, db: Session = Depends(get_db)):
    create_item(db, item)
    return {"status": "inserted"}

@app.get("/items/all")
def get_items_endpoint(db: Session = Depends(get_db)):
    return read_items(db)