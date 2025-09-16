
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models.wallet import WalletCreate, WalletUpdate
from app.infrastructure.database.fx_database import get_db_session
from app.domain.services.common import create
from app.infrastructure.models.wallet import Wallet
from app.infrastructure.repositories.common import get_entity_by_filter


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


@router.post("/{user_id}/fund", status_code=status.HTTP_200_OK)
async def fund_wallet(
    user_id: int,
    wallet_request: WalletUpdate,
    session: Annotated[AsyncSession, Depends(get_db_session)]
):
    """
    Fund an existing wallet.
    """
    if wallet_request.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be greater than zero")
    try:
        wallet = await get_entity_by_filter(session, Wallet, user_id=user_id, currency=wallet_request.currency)
        if not wallet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wallet not found")

        wallet.balance += wallet_request.amount
        await session.commit()
        return wallet
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

