
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models.wallet import WalletCreate
from app.infrastructure.database.fx_database import get_db_session
from app.domain.services.common import create
from app.infrastructure.models.wallet import Wallet


router = APIRouter(
    prefix="/v1/wallets",
    tags=["Wallets"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_wallet(
    wallet: WalletCreate,
    session: Annotated[AsyncSession, Depends(get_db_session)]
):
    """
    Create a new wallet.
    """
    try:
        return await create(session, wallet, Wallet)
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))