from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import SessionLocal
from crud import *
from schemas import Item

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

@app.post("/items/create")
def create_item_endpoint(item: Item, db: Session = Depends(get_db)):
    create_item(item, db)
    return {"status": "inserted"}

@app.get("/items/read_all")
def get_items_endpoint(db: Session = Depends(get_db)):
    return read_items(db)

@app.post("/items/read_matching")
def post_matching_items_endpoint(item: Item, db: Session = Depends(get_db)):
    return read_matching(item, db)

@app.put("/items/{item_id}")
def update_endpoint(
    item_id: int,
    item: Item,
    db: Session = Depends(get_db)
):
    return update_item(item_id, item, db)

@app.delete("/items/{item_id}")
def delete_endpoint(
    item_id: int,
    db: Session = Depends(get_db)
):
    return delete_item(item_id, db)