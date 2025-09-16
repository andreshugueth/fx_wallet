import pytest

pytestmark = pytest.mark.anyio

async def test_create_user_success(test_app):
    payload = {"name": "John Doe", "username": "johndoe"}
    response = await test_app.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["username"] == "johndoe"
    assert "id" in data
    assert "created_at" in data


async def test_create_user_missing_fields(test_app):
    payload = {"name": "John Doe"}  # missing username
    response = await test_app.post("/users/", json=payload)
    assert response.status_code == 422


async def test_create_user_duplicate_username(test_app):
    payload = {"name": "Jane Doe", "username": "johndoe"}  # assuming johndoe already exists
    response = await test_app.post("/users/", json=payload)
    assert response.status_code == 400


async def test_create_user_empty_username(test_app):
    payload = {"name": "Empty User", "username": ""}
    response = await test_app.post("/users/", json=payload)
    assert response.status_code == 422


