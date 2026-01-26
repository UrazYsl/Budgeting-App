# Budgeting-App
A full-stack personal budgeting app with a FastAPI backend hosted on an Ubuntu server and a Flutter Android client. Tracks expenses, income, and category-based summaries with secure REST APIs and a clean mobile UI.

Stack: Kotlin, FastAPI, PostgreSQL, Ubuntu

Python Packages:
- fastapi
- uvicorn
- sqlalchemy
- psycopg[binary]

## Running the Backend (Development)

1. Create a virtual environment (recommended)
2. Install dependencies
3. Run the FastAPI server:

```bash
uvicorn main:app --reload

See [`docs/roadmap.md`](docs/roadmap.md) for the development plan.