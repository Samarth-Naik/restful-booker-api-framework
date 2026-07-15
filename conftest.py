import requests
import pytest
from config.config import BASE_URL

@pytest.fixture
def auth_token():

    payload={
    "username" : "admin",
    "password" : "password123"
    }

    response=requests.post(f"{BASE_URL}/auth",json=payload)

    return response.json()["token"]