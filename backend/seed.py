from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy import text
from models import Base, Category, Account


def seed_db(db: Session) -> None:
    # demonstrate using the generic helper instead of hard‑coding
    items = {}
    items[Category] = ["Misc", "Food", "Transport", "Entertainment"]
    items[Account] = ["Checking", "Savings", "Credit Card", "Cash"]
    for model, item_list in items.items():
        for item in item_list:
            seed_items(db, model, item)
    db.commit()


def seed_items(db: Session, model: Type[Base], item: str) -> None:
    # Check if given item already exists
    existing = db.query(model).filter(model.name == item).first()
    if not existing:
        db.add(model(name=item)) 