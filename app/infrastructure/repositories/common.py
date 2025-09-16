


from typing import TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

TORM = TypeVar("TORM")


async def insert_entity(session: AsyncSession, entity: TORM) -> TORM:
    session.add(entity)
    await session.flush()
    await session.refresh(entity)
    return entity


async def get_entity_by_filter(session: AsyncSession, model: type[TORM], **filters) -> TORM | None:
    result = await session.execute(
        select(model).filter_by(**filters)
    )
    return result.scalars().one_or_none()


async def update_entity(session: AsyncSession, entity: TORM, orm_model: type[TORM], **updates) -> TORM:

    if not isinstance(entity, orm_model):
        raise ValueError("Entity is not of the correct type")

    entity_id = getattr(entity, "id", None)
    if entity_id is None:
        raise ValueError("Entity does not have an 'id' attribute")

    db_entity = await session.get(orm_model, entity_id)
    if db_entity is None:
        raise ValueError("Entity not found in the database")

    for key, value in updates.items():
        setattr(db_entity, key, value)
    session.add(db_entity)
    await session.flush()
    await session.refresh(db_entity)
    return db_entity

