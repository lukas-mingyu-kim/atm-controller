# Sign In

Sign in & get token.

**URL** : `/auth/signin`

**Method** : `POST`

**Request Body**:

| **Field Name** | **Type** | **Sample Value**   |
|----------------|----------|--------------------|
| card_num       | string   | "1111222233334444" |
| pin_num        | string   | "123456"           |


## Sample Requests
(Use card_num `1111222233334444` to use dummy data.)
```
curl --location --request POST 'http://localhost:8000/auth/signin' \
--header 'Content-Type: application/json' \
--data-raw '{
    "card_num": "1111222233334444",
    "pin_num": "123456"
}'
```

## Success Response

**Code** : `200 OK`

```json
{
    "user_id": 1,
    "token": "6a01dcd1554df1c23ea435c930a30c7f49f8b6b0"
}
```
*Token expiration is set to 3 minutes.
