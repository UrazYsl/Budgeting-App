from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, model_validator

class Interval(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"

class AccountCreate(BaseModel):
    name: str

class AccountOut(AccountCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str

class CategoryOut(CategoryCreate):
    id: int

class TransactionCreate(BaseModel):
    date: date
    amount: float = Field(gt=0)
    account_id: int
    category_id: int
    recurring: bool = False
    recurring_interval: Interval | None = None

    @model_validator(mode="after")
    def recurring_rules(self):
        if self.recurring and self.recurring_interval is None:
            raise ValueError("recurring_interval is required when recurring=True")
        if not self.recurring and self.recurring_interval is not None:
            raise ValueError("recurring_interval must be None when recurring=False")
        return self

class TransactionOut(TransactionCreate):
    id: int
