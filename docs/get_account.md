# Get an Account

Get an account. A user can only access their own accounts.

**URL** : `/api/accounts/<account_id>`

**Method** : `GET`

**Header**:

| **Field Name** | **Type** | **Sample Value**   |
|----------------|----------|--------------------|
| Authorization  | string   | "Token {Token from signin API}" |


## Sample Requests
- Use a token from [Sign In](docs/sign_in.md) API.
- Use an account_id from [List Accounts](docs/list_account.md) API. 
```
curl --location --request GET 'http://localhost:8000/api/accounts/27844244561998155395' \
--header 'Authorization: Token b63c1df3e4d32f55a6d49f3d28f6c515960bcacf'
```

## Success Response

**Code** : `200 OK`

```json
{
    "account_num": "27844244561998155395",
    "user": 1,
    "balance": 21697
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
