from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.models.user import UserCreate
from typing import Annotated
from app.infrastructure.models.user import User
from app.domain.services.common import create
from app.infrastructure.database.fx_database import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    prefix="/v1/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: Annotated[AsyncSession, Depends(get_db_session)]):
    """
    Create a new user.
    """
    try:
        return await create(session, user, User)
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
