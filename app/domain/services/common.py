from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import Type, TypeVar
from fastapi.exceptions import HTTPException
from fastapi import status

from app.domain.utils.helper import pydantic_to_orm
from app.infrastructure.repositories.common import insert_entity

TORM = TypeVar("TORM")


async def create(session: AsyncSession, pydantic_model: BaseModel, orm_model: Type[TORM], **kwargs) -> TORM:
    """
    Generic function to create an ORM model instance from a Pydantic model.
    """
    orm_obj, _ = await pydantic_to_orm(pydantic_model, orm_model, **kwargs)
    try:
        return await insert_entity(session, orm_obj)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
