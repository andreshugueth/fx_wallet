
from pydantic import BaseModel
from datetime import datetime

from app.domain.models.wallet import Wallet

class User(BaseModel):
    id: int
    name: str
    username: str
    wallets: list[Wallet] = []
    created_at: datetime
