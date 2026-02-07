# Budgeting App - Roadmap

**Stack:** Kotlin (Android) + FastAPI (Python) + PostgreSQL  
**Goal:** Track income and expenses on mobile, synced to your own server.

---

## MVP Goal

When done, you'll be able to:
- Add/edit transactions (income & expenses)
- Organize by accounts (cards, cash) and categories
- See monthly summaries
- View transaction history

---

## Phase 1: Backend Setup (Complete)

### Step 1: Get FastAPI Running
- [X] Create FastAPI app (`main.py`)
- [X] Add `/health` endpoint
- [X] Run locally and see it working

### Step 2: Database Connection
- [X] Install PostgreSQL (or use local/cloud)
- [X] Connect FastAPI to database
- [X] Test connection works

### Step 3: Basic Transaction CRUD
- [X] Create a method to add to table
- [X] Create a method to read table contents
- [X] Create a method to update content from table
- [X] Create a method to delete content from table

### Step 4: Finalize Transaction Data Format
- [X] Finalize JSON format (what the Android app sends/receives)
- [X] Update Functions & table columns to match the finalized format

### Step 5: Database Models
- [X] Create Account model
- [X] Create Category model
- [X] Create Transaction model

### Step 6: One Simple Endpoint
- [X] Create endpoint to add a transaction (no auth yet)
- [X] Test it works
- [X] See data in database

---

## What's Next (Later)
**Phase 2:** Create an initializer (Setup databases etc.)
**Phase 3:** More endpoints (accounts, categories CRUD)
**Phase 4:** Automated tables(CRUD for tables)  
**Phase 5:** Android app  
**Phase 6:** Deploy to server
