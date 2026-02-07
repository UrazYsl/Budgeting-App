from database import SessionLocal, engine

import models

def init_db():
    """Create all tables from models if they don't exist. Call at app startup."""
    models.Base.metadata.create_all(bind=engine)
