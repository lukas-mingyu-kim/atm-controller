# List Accounts

List all accounts of the user.

**URL** : `/api/accounts`

**Method** : `GET`

**Header**:

| **Field Name** | **Type** | **Sample Value**   |
|----------------|----------|--------------------|
| Authorization  | string   | "Token {Token from signin API}" |


## Sample Requests
Use a token from [Sign In](docs/sign_in.md) API.
```
curl --location --request GET 'http://localhost:8000/api/accounts' \
--header 'Authorization: Token 6a01dcd1554df1c23ea435c930a30c7f49f8b6b0'
```

## Success Response

**Code** : `200 OK`

```json
{
    "accounts": [
        "87122597970631231070",
        "27844244561998155395",
        "62927951588081279245",
        "89677259494215578897",
        "93002907186119097881"
    ]
}
```

## Error Response

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
