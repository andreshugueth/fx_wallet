import pytest

pytestmark = pytest.mark.anyio

async def test_fund_wallet_success(test_app):
    user_id = "user123" # assuming we have a user with this ID
    payload = {"currency": "USD", "amount": 1000.0}
    response = await test_app.post(f"/wallets/{user_id}/fund", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["balances"]["USD"] == 1000.0


async def test_fund_wallet_invalid_currency(test_app):
    user_id = "user123"
    payload = {"currency": "INVALID", "amount": 1000.0}
    response = await test_app.post(f"/wallets/{user_id}/fund", json=payload)
    assert response.status_code == 400


async def test_fund_wallet_negative_amount(test_app):
    user_id = "user123"
    payload = {"currency": "USD", "amount": -50.0}
    response = await test_app.post(f"/wallets/{user_id}/fund", json=payload)
    assert response.status_code == 400


async def test_fund_wallet_missing_fields(test_app):
    user_id = "user123"
    payload = {"currency": "USD"}  # missing amount
    response = await test_app.post(f"/wallets/{user_id}/fund", json=payload)
    assert response.status_code == 422  # Unprocessable Entity (validation error) by pydantic
