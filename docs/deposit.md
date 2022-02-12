# Deposit to an Account

Deposit to an account of a user, and update the balance.

**URL** : `/api/accounts/<account_id>/deposit`

**Method** : `PATCH`

**Header**:

| **Field Name** | **Type** | **Sample Value**   |
|----------------|----------|--------------------|
| Authorization  | string   | "Token {Token from signin API}" |

**Request Body**:

| **Field Name** | **Type** | **Sample Value**   |
|----------------|----------|--------------------|
| amount         | integer   | 1000 |

## Sample Requests
- Use a token from [Sign In](docs/sign_in.md) API.
- Use an account_id from [List Accounts](docs/list_account.md) API. 
```
curl --location --request PATCH 'http://localhost:8000/api/accounts/87122597970631231070/deposit' \
--header 'Authorization: Token 6a01dcd1554df1c23ea435c930a30c7f49f8b6b0' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": 1000
}'
```

## Success Response

**Code** : `200 OK`

```json
{
    "account_num": "87122597970631231070",
    "user": 1,
    "balance": 20150
}
```


## Error Response

**Code** : `404 Not Found`

```json
{
    "detail": "Given account number (2784424456199815539) for this user does not exist."
}
```

**Code** : `401 Unauthorized`

```json
{
    "detail": "Token has expired"
}
```
or
```json
{
    "detail": "Invalid token"
}
```

