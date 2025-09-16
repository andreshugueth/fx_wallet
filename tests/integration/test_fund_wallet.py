import pytest

pytestmark = pytest.mark.anyio

async def test_fund_wallet_success(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP", "amount": 1000.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/fund", json=payload)
    assert response.status_code == 200
    assert response.json()["user_id"] == create_test_user["id"]
    assert response.json()["balance"] == 1100.0



async def test_fund_wallet_invalid_currency(test_app, create_test_user, create_test_wallet):
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/fund", json={"currency": "INVALID", "amount": 1000.0})
    assert response.status_code == 422


async def test_fund_wallet_negative_amount(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP", "amount": -50.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/fund", json=payload)
    assert response.status_code == 400


async def test_fund_wallet_missing_fields(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP"}  # missing amount
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/fund", json=payload)
    assert response.status_code == 422
