

from datetime import datetime, timezone
from decimal import Decimal
from app.domain.models.user import User
from app.domain.models.wallet import Currency
from app.infrastructure.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    currency: Mapped[Currency] = mapped_column(nullable=False)
    balance: Mapped[Decimal] = mapped_column(nullable=False, default=0.0)
    user_id: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="wallets", foreign_keys=[user_id])
