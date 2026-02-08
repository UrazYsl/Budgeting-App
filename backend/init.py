import os
import models
from database import engine  # <-- use your existing app engine (tables)


def create_tables() -> None:
    models.Base.metadata.create_all(bind=engine)  # <-- uses database.py engine


def init_db() -> None:
    if os.getenv("DATABASE_URL"):
        create_tables()
        return
    create_tables()
