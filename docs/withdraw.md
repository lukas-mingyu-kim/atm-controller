# Withdraw from an Account

Withdraw from an account of a user if the balance is sufficient, and update the balance .

**URL** : `/api/accounts/<account_id>/withdraw`

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
curl --location --request PATCH 'http://localhost:8000/api/accounts/83274552548730878040/withdraw' \
--header 'Authorization: Token d6ffb8b663ee6c340cf431b39d2966c82245a062' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": 1000
}'
```

## Success Response

**Code** : `200 OK`

```json
{
    "account_num": "83274552548730878040",
    "user": 1,
    "balance": 5739
}
```


## Error Response

**Code** : `422 Unprocessable Entity`

```json
{
    "detail": "Balance not sufficient."
}
```

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

