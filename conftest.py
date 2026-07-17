import requests
import pytest
from config.config import BASE_URL
from utils.payloads import create_booking_payload,auth_payload

@pytest.fixture
def auth_token():

    payload=auth_payload
    response=requests.post(f"{BASE_URL}/auth",json=payload)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture
def create_booking():
    
    payload=create_booking_payload
    response=requests.post(f"{BASE_URL}/booking",json=payload)
    assert response.status_code == 200
    return response.json(),payload