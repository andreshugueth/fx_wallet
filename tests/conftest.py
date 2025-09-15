import pytest
from app.api import app
from httpx import AsyncClient, ASGITransport

@pytest.fixture(scope="session")
async def test_app():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as test_client:
        yield test_client


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
