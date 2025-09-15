import pytest

pytestmark = pytest.mark.anyio


async def test_health_check(test_app):
    response = await test_app.get("/ping/")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
