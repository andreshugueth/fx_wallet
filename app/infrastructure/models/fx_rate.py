

from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import DateTime
from app.domain.models.wallet import Currency
from app.infrastructure.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class FXRate(Base):
    __tablename__ = "fx_rate"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_currency: Mapped[Currency] = mapped_column(nullable=False)
    to_currency: Mapped[Currency] = mapped_column(nullable=False)
    rate: Mapped[Decimal] = mapped_column(nullable=False)
    last_updated: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), nullable=False)
