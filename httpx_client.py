import time
import httpx

data = {
  "email": f"{time.time()}@example.com",
  "lastName": "Hello",
  "firstName": "From",
  "middleName": "Postman",
  "phoneNumber": "+19999999999"
}

client = httpx.Client(base_url="http://localhost:8003", timeout=5)

response = client.post("/api/v1/users", json=data)
print(response.json())
