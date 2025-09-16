from typing import Type, TypeVar
from pydantic import BaseModel

TORM = TypeVar("TORM")


async def pydantic_to_orm(
    pydantic_instance: BaseModel,
    orm_model: Type[TORM],
    exclude: set[str] | None = None,
    include: set[str] | None = None,
    **kwargs,
) -> tuple[TORM, dict]:
    """
    Convert a Pydantic model instance to an ORM model instance.

    Args:
        pydantic_instance (BaseModel): The Pydantic model instance.
        orm_model (Type[TORM]): The ORM model class.
        exclude (set[str] | None, optional): Fields to exclude. Defaults to None.
        include (set[str] | None, optional): Fields to include. Defaults to None.
        **kwargs: Additional fields for the ORM model.

    Returns:
        tuple[TORM, dict]: The ORM model instance and the data dictionary.
    """
    data = {
        **pydantic_instance.model_dump(
            exclude_unset=True, exclude=exclude, include=include
        ),
        **kwargs,
    }
    return orm_model(**data), data