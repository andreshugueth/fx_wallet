from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

from app.domain.models.wallet import Currency


class FXRate(BaseModel):
    from_currency: Currency
    to_currency: Currency
    rate: Decimal
    last_updated: datetime
