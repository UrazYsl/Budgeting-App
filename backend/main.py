from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel

from database import SessionLocal

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
def create_item(item: Item, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO items (name, description, price, tax)
        VALUES (:name, :description, :price, :tax)
    """)

    db.execute(
        query,
        {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax,
        }
    )

    db.commit()

    return {"status": "inserted"}