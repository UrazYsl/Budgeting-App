from sqlalchemy.orm import Session
from sqlalchemy import text

def create_account(account, db: Session):
    result = db.execute(
        text("""
            INSERT INTO accounts (name)
            VALUES (:name)
            RETURNING id, name
        """),
        {"name": account.name},
    )
    db.commit()
    return result.mappings().one()

def read_accounts(db: Session):
    result = db.execute(text("SELECT id, name FROM accounts ORDER BY id"))
    return result.mappings().all()

def delete_account(account_id: int, db: Session):
    # If FK is ON DELETE CASCADE on transactions.account_id,
    # this will delete related transactions automatically.
    result = db.execute(
        text("DELETE FROM accounts WHERE id = :id"),
        {"id": account_id},
    )
    db.commit()
    return result.rowcount


def create_category(category, db: Session):
    result = db.execute(
        text("""
            INSERT INTO categories (name)
            VALUES (:name)
            RETURNING id, name
        """),
        {"name": category.name},
    )
    db.commit()
    return result.mappings().one()

def read_categories(db: Session):
    result = db.execute(text("SELECT id, name FROM categories ORDER BY id"))
    return result.mappings().all()

def delete_category(category_id: int, db: Session):
    # If FK is ON DELETE SET DEFAULT on transactions.category_id
    # and the default is Misc, transactions will be reassigned.
    result = db.execute(
        text("DELETE FROM categories WHERE id = :id"),
        {"id": category_id},
    )
    db.commit()
    return result.rowcount


def create_transaction(tx, db: Session):
    result = db.execute(
        text("""
            INSERT INTO transactions (date, amount, account_id, category_id)
            VALUES (:date, :amount, :account_id, :category_id)
            RETURNING id, date, amount, account_id, category_id
        """),
        {
            "date": tx.date,
            "amount": tx.amount,
            "account_id": tx.account_id,
            "category_id": tx.category_id,
        },
    )
    db.commit()
    return result.mappings().one()

def read_transactions(db: Session):
    result = db.execute(
        text("""
            SELECT id, date, amount, account_id, category_id
            FROM transactions
            ORDER BY date DESC, id DESC
        """)
    )
    return result.mappings().all()

def delete_transaction(tx_id: int, db: Session):
    result = db.execute(
        text("DELETE FROM transactions WHERE id = :id"),
        {"id": tx_id},
    )
    db.commit()
    return result.rowcount


def create_recurring_transaction(rtx, db: Session):
    result = db.execute(
        text("""
            INSERT INTO recurring_transactions
                (amount, recurring_interval, next_run_date, account_id, category_id)
            VALUES (:amount, :recurring_interval, :next_run_date, :account_id, :category_id)
            RETURNING id, amount, recurring_interval, next_run_date, account_id, category_id
        """),
        {
            "amount": rtx.amount,
            "recurring_interval": rtx.recurring_interval.value,
            "next_run_date": rtx.next_run_date,
            "account_id": rtx.account_id,
            "category_id": rtx.category_id,
        },
    )
    db.commit()
    return result.mappings().one()

def read_recurring_transactions(db: Session):
    result = db.execute(
        text("""
            SELECT id, amount, recurring_interval, next_run_date, account_id, category_id
            FROM recurring_transactions
            ORDER BY next_run_date ASC, id ASC
        """)
    )
    return result.mappings().all()

def delete_recurring_transaction(rtx_id: int, db: Session):
    result = db.execute(
        text("DELETE FROM recurring_transactions WHERE id = :id"),
        {"id": rtx_id},
    )
    db.commit()
    return result.rowcount
