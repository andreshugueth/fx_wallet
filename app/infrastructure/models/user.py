


from datetime import datetime, timezone

from sqlalchemy import DateTime
from app.infrastructure.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.models.wallet import Wallet


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        nullable=False
    )

    wallets: Mapped[list[Wallet]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin",
        foreign_keys=[Wallet.user_id],
    )
