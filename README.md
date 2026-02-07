# Budgeting-App

A full-stack personal budgeting app with a FastAPI backend and an Android client (Kotlin). Tracks income, expenses, accounts, and categories with REST APIs and sync to your own server.

**Stack:** Kotlin (Android), FastAPI (Python), PostgreSQL

## Status

- **Phase 1 (Backend setup):** ✓ Complete — FastAPI app, DB connection, CRUD, schemas, database models (Account, Category, Transaction), and transaction endpoint.
- **Next:** Phase 2 — Initializer (setup databases, create tables). See [docs/roadmap.md](docs/roadmap.md) for the full plan.

## Python packages

- fastapi
- uvicorn
- sqlalchemy
- psycopg[binary]

## Running the backend (development)

1. Create a virtual environment (recommended).
2. Install dependencies.
3. From the `backend` directory, run:

```bash
cd backend
uvicorn main:app --reload
```

See [docs/roadmap.md](docs/roadmap.md) for the full development plan.