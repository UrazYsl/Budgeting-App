# Budgeting-App

A full-stack personal budgeting app with a FastAPI backend and an Android client (Kotlin). Tracks income, expenses, accounts, and categories with REST APIs and sync to your own server.

**Stack:** Kotlin (Android), FastAPI (Python), PostgreSQL

## Status

- **Phase 1 (Backend setup):** Complete — FastAPI app, DB connection, CRUD, schemas, database models (Account, Category, Transaction), and transaction endpoint.
- **Next:** Phase 2 — Initializer (setup databases, create tables). See [docs/roadmap.md](docs/roadmap.md) for the full plan.

## Python packages

- fastapi
- uvicorn
- sqlalchemy
- psycopg[binary]


## Prerequisites

Before running the backend, ensure the following are installed:

- Python 3.10+
- PostgreSQL (server running locally)

You can verify PostgreSQL is installed by running:

```bash
psql --version
```

## Create the Database

Currently, the PostgreSQL database must be created manually:

```bash
createdb budgeting_app
```

## Database Setup

The backend uses PostgreSQL.
Make sure PostgreSQL is running and your `DATABASE_URL` (or connection settings in `database.py`) point to the correct database.

### Option 1 — Automatic (Recommended)
From the `backend` directory, run:
```bash
uvicorn main:app --reload
```

### Option 2 — Manual Initialization
From the `backend` directory, run:
```bash
python -m backend.init_db
uvicorn main:app --reload
```



## Running The Backend (Development)
1. Create a virtual environment (recommended).
2. Install dependencies listed above.
3. Start the server using either of the options listed above.

## API docs will be available at: http://127.0.0.1:8000/docs


## Health Check
To test database connectivity, check http://127.0.0.1:8000/health/db
You should see "{ "ok": true }" if the database is connected.

See [docs/roadmap.md](docs/roadmap.md) for the full development plan.

