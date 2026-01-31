from sqlalchemy.orm import Session
from sqlalchemy import text


#CREATE
def create_item(item, db: Session):
    query = text("""
        INSERT INTO items (name, price)
        VALUES (:name, :price)
    """)

    db.execute(
        query,
        {
            "name": item.name,
            "price": item.price
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
              AND price = :price
        """),
        {
            "name": item.name,
            "price": item.price
        }
    )
    return result.mappings().all()

#UPDATE
def update_item(item_id: int, item, db: Session):
    result = db.execute(
        text("""
            UPDATE items
            SET name = :name,
                price = :price
            WHERE id = :id
        """),
        {
            "id": item_id,
            "name": item.name,
            "price": item.price
        }
    )

    db.commit()
    return result.rowcount

#DELETE
def delete_item(item_id: int, db: Session):
    result = db.execute(
        text("""
            DELETE FROM items
            WHERE id = :id;
        """),
        {"id": item_id}
    )

    db.commit()
    return result.rowcount