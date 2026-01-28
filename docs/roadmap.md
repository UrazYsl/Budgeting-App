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

## Current Focus: Backend Setup

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
- [] Create a method to update content from table
- [] Create a method to delete content from table

### Step 4: Database Models
- [ ] Create User model
- [ ] Create Account model
- [ ] Create Category model
- [ ] Create Transaction model

### Step 5: One Simple Endpoint
- [ ] Create endpoint to add a transaction (no auth yet)
- [ ] Test it works
- [ ] See data in database

---

## What's Next (Later)
**Phase 2:** Create an initializer (Setup databases etc.)
**Phase 3:** Add authentication (login/register)  
**Phase 4:** More endpoints (accounts, categories CRUD)  
**Phase 5:** Android app  
**Phase 6:** Deploy to server
