
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

from app.domain.models.wallet import Wallet

class User(BaseModel):
    id: int
    name: str
    username: str
    wallets: list[Wallet] = []
    created_at: datetime

class UserResponse(User):
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str
    username: str = Field(..., min_length=1)
