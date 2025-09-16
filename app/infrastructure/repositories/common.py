


from typing import TypeVar
from sqlalchemy.ext.asyncio import AsyncSession

TORM = TypeVar("TORM")


async def insert_entity(session: AsyncSession, entity: TORM) -> TORM:
    session.add(entity)
    await session.flush()
    await session.refresh(entity)
    return entity
