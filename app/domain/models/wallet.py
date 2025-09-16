from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from enum import Enum


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    COP = "COP"
    MXN = "MXN"


class Wallet(BaseModel):
    id: int
    user_id: int
    currency: Currency
    balance: Decimal
    created_at: datetime
    updated_at: datetime
