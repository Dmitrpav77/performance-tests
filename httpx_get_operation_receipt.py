import time
import httpx

data = {
  "email": f"{time.time()}@example.com",
  "lastName": "Hello",
  "firstName": "From",
  "middleName": "Postman",
  "phoneNumber": "+19999999999"
}

create_new_user = httpx.post("http://localhost:8003/api/v1/users", json=data)
created_user_id = create_new_user.json()["user"]["id"]

credit_account_payload_data = {
    "userId": created_user_id
}

create_credit_account = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=credit_account_payload_data)
created_credit_account_id = create_credit_account.json()["account"]["id"]
created_credit_card_id = create_credit_account.json()["account"]["cards"][0]["id"]

make_purchase_upload_data = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": created_credit_card_id,
  "accountId": created_credit_account_id,
  "category": "taxi"
}

make_purchase = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_upload_data)

operation_id = make_purchase.json()["operation"]["id"]

get_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
print(get_receipt.json())


