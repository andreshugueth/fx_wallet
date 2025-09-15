# FX wallet

## System Context

Prototype multi-currency system that allows clients to:

- Fund wallets in different currencies
- Convert between currencies using FX rates (fixed)
- Withdraw funds to external bank accounts
- View wallet balances

## Interface Model

### Fund Wallet

- **Endpoint**: `POST /wallets/<user_id>/fund`

Input

```json
{
  "currency": "USD",
  "amount": 1000.0
}
```

### Convert Currency

- **Endpoint**: `POST /wallets/<user_id>/convert`
  Input

```json
{
  "from_currency": "USD",
  "to_currency": "MXN",
  "amount": 500.0
}
```

### Withdraw Funds

- **Endpoint**: `POST /wallets/<user_id>/withdraw`

Input

```json
{
  "currency": "MXN",
  "amount": 300.0
}
```

### View Balances

- **Endpoint**: `GET /wallets/<user_id>/balances`
  Output

```json
{
  "USD": 500.0,
  "MXN": 200.0
}
```

## Decision Log

- No, authentication/authorization for prototype
- All amounts are positive numbers and use two decimal places
- FX rates are hard coded
- Only USD, MXN, EUR, and COP are supported
- No transaction fees are applicable
- No timezone or date handling for transactions, all dates will be UTC
- No communication with external bank account implementation
