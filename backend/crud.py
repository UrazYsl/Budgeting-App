from sqlalchemy.orm import Session
from sqlalchemy import text


#CREATE
def create_item(db: Session, item):
    query = text("""
        INSERT INTO items (name, description, price, tax)
        VALUES (:name, :description, :price, :tax)
    """)

    db.execute(
        query,
        {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax,
        }
    )

    db.commit()

#READ-ALL
def read_items(db: Session):
    result = db.execute(text("SELECT * FROM items"))
    return result.mappings().all()

#READ-MATCHING
def read_matching(item, db: Session):
    result = db.execute(
        text("""
            SELECT *
            FROM items
            WHERE name = :name
              AND description IS NOT DISTINCT FROM :description
              AND price = :price
              AND tax IS NOT DISTINCT FROM :tax
        """),
        {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax,
        }
    )
    return result.mappings().all()

#UPDATE
def update_item(item_id: int, item, db: Session):
    result = db.execute(
        text("""
            UPDATE items
            SET name = :name,
                description = :description,
                price = :price,
                tax = :tax
            WHERE id = :id
        """),
        {
            "id": item_id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax,
        }
    )

    db.commit()
    return result.rowcount
