from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session
from asyncio import current_task

DB_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


engine = create_async_engine(DB_URL)
Session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db_session():
    session = async_scoped_session(Session, scopefunc=current_task)
    try:
        yield session
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
