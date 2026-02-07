from sqlalchemy import (
    Column, Integer, String, Date, Float, Boolean, ForeignKey, text
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    # delete account => delete its transactions (DB FK handles it)
    transactions = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete",
        passive_deletes=True,
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    transactions = relationship(
        "Transaction",
        back_populates="category",
        passive_deletes=True,
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)

    # account delete -> cascade
    account_id = Column(
        Integer,
        ForeignKey("accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # category delete -> set default (Misc)
    # IMPORTANT: the DB column must have a DEFAULT set to Misc id in SQL
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="SET DEFAULT"),
        nullable=False,
        index=True,
    )

    recurring = Column(Boolean, nullable=False, server_default=text("false"))
    recurring_interval = Column(String, nullable=True)

    account = relationship("Account", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
