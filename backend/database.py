from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from local_settings import postgresql as settings

DATABASE_URL = f"postgresql+psycopg://{settings['pguser']}:{settings['pgpassword']}@{settings['pghost']}:{settings['pgport']}/{settings['pgdb']}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
