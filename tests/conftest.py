import pytest
from app.api import app
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.infrastructure.models.base import Base

TEST_DB_URL = "postgresql+asyncpg://test_user:test_password@localhost:5433/test_db"

engine = create_async_engine(TEST_DB_URL)
SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

@pytest.fixture(scope="session")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture(scope="session")
async def session(setup_database):
    async with SessionLocal() as session:
        yield session


@pytest.fixture(scope="session")
async def test_app():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as test_client:
        yield test_client


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
