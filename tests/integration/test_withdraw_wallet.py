
import pytest

pytestmark = pytest.mark.anyio

async def test_withdraw_from_nonexistent_wallet(test_app, create_test_user):
    payload = {"currency": "COP", "amount": 100.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/withdraw", json=payload)
    assert response.status_code == 404


async def test_withdraw_insufficient_funds(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP", "amount": 200.0}  # more than the 100.0 balance
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/withdraw", json=payload)
    assert response.status_code == 400


async def test_withdraw_success(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP", "amount": 50.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/withdraw", json=payload)
    assert response.status_code == 200
    assert response.json()["balance"] == 50.0
    assert response.json()["user_id"] == create_test_user["id"]


async def test_withdraw_invalid_currency(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "INVALID", "amount": 50.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/withdraw", json=payload)
    assert response.status_code == 422


async def test_withdraw_negative_amount(test_app, create_test_user, create_test_wallet):
    payload = {"currency": "COP", "amount": -10.0}
    response = await test_app.post(f"/v1/wallets/{create_test_user['id']}/withdraw", json=payload)
    assert response.status_code == 400

