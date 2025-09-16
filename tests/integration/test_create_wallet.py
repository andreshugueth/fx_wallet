import pytest
from decimal import Decimal

pytestmark = pytest.mark.anyio


async def test_create_wallet_success(test_app, create_test_user):
    payload = {
        "user_id": create_test_user["id"],
        "currency": "USD",
        "balance": 0.0,
    }
    response = await test_app.post("/v1/wallets/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == create_test_user["id"]
    assert "id" in data
    assert "created_at" in data

async def test_create_wallet_missing_fields(test_app, create_test_user):
    payload = {
        "user_id": create_test_user["id"],
        # "currency" is missing
        "balance": 0.0,
    }
    response = await test_app.post("/v1/wallets/", json=payload)
    assert response.status_code == 422

async def test_create_wallet_invalid_currency(test_app, create_test_user):
    payload = {
        "user_id": create_test_user["id"],
        "currency": "INVALID",  # invalid currency
        "balance": 0.0,
    }
    response = await test_app.post("/v1/wallets/", json=payload)
    assert response.status_code == 422