from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import SessionLocal
import crud
from schemas import (
    AccountCreate, AccountOut,
    CategoryCreate, CategoryOut,
    TransactionCreate, TransactionOut,
)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    return {"ok": db.execute(text("select 1")).scalar_one() == 1}


@app.post("/accounts", response_model=AccountOut)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(account, db)

@app.get("/accounts", response_model=list[AccountOut])
def read_accounts_endpoint(db: Session = Depends(get_db)):
    return crud.read_accounts(db)

@app.delete("/accounts/{account_id}")
def delete_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_account(account_id, db)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"deleted": deleted, "warning": "Associated transactions were deleted (cascade)."}


@app.post("/categories", response_model=CategoryOut)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(category, db)

@app.get("/categories", response_model=list[CategoryOut])
def read_categories_endpoint(db: Session = Depends(get_db)):
    return crud.read_categories(db)

@app.delete("/categories/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_category(category_id, db)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"deleted": deleted, "note": "Transactions were reassigned to Misc (default category)."}


@app.post("/transactions", response_model=TransactionOut)
def create_transaction_endpoint(tx: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(tx, db)

@app.get("/transactions", response_model=list[TransactionOut])
def read_transactions_endpoint(db: Session = Depends(get_db)):
    return crud.read_transactions(db)

@app.delete("/transactions/{tx_id}")
def delete_transaction_endpoint(tx_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_transaction(tx_id, db)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"deleted": deleted}
