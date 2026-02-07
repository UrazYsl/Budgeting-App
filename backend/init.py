from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

import models
from database import engine  # <-- use your existing app engine (tables)
from local_settings import postgresql


def create_db() -> None:
    db_name = postgresql["pgdb"]

    # Admin connection to a DB that always exists
    admin_url = URL.create(
        "postgresql+psycopg",
        username=postgresql["pguser"],
        password=postgresql["pgpassword"],
        host=postgresql["pghost"],
        port=postgresql["pgport"],
        database="postgres",
    )

    admin_engine = create_engine(admin_url)

    with admin_engine.connect() as conn:
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")

        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :name"),
            {"name": db_name},
        ).scalar()

        if not exists:
            conn.execute(text(f'CREATE DATABASE "{db_name}"'))


def create_tables() -> None:
    models.Base.metadata.create_all(bind=engine)  # <-- uses database.py engine


def init_db() -> None:
    create_db()
    create_tables()
