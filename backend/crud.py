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
            INSERT INTO transactions
                (date, amount, account_id, category_id, recurring, recurring_interval)
            VALUES
                (:date, :amount, :account_id, :category_id, :recurring, :recurring_interval)
            RETURNING id, date, amount, account_id, category_id, recurring, recurring_interval
        """),
        {
            "date": tx.date,
            "amount": tx.amount,
            "account_id": tx.account_id,
            "category_id": tx.category_id,
            "recurring": tx.recurring,
            "recurring_interval": tx.recurring_interval,
        },
    )
    db.commit()
    return result.mappings().one()

def read_transactions(db: Session):
    result = db.execute(
        text("""
            SELECT id, date, amount, account_id, category_id, recurring, recurring_interval
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
