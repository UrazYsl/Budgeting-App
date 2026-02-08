"""
This script ensures that the database tables are created.
It is another way to initialize the tables manually.
"""
from init import init_db

if __name__ == "__main__":
    init_db()
    print("Database tables ensured.")
