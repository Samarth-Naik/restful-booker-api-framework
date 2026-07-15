import requests
from config.config import BASE_URL

def test_create_token():

    payload={
    "username" : "admin",
    "password" : "password123"
    }

    response=requests.post(f"{BASE_URL}/auth",payload)

    assert response.status_code == 200
    data=response.json()

    assert "token" in data
    assert isinstance(data["token"],str)
    assert data["token"] is not None