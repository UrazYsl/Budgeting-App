import os
import models
from database import engine
from seed import seed_db


def create_tables() -> None:
    models.Base.metadata.create_all(bind=engine)

def init_db() -> None:
    create_tables()
    seed_db(models.SessionLocal())
    db.close()