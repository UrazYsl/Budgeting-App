import os
import models
from database import engine, SessionLocal
from seed import seed_db


def create_tables() -> None:
    models.Base.metadata.create_all(bind=engine)

def init_db() -> None:
    create_tables()
    db = SessionLocal()
    try:
        seed_db(db)
    finally:
        db.close()