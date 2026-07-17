import requests
import pytest
from config.config import BASE_URL
from utils.payloads import create_booking_payload,auth_payload
from utils.api_client import ApiClient

@pytest.fixture
def auth_token():

    payload=auth_payload
    response=ApiClient.post(f"{BASE_URL}/auth",payload)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture
def create_booking():
    
    payload=create_booking_payload
    response=ApiClient.post(f"{BASE_URL}/booking",payload)
    assert response.status_code == 200
    return response.json(),payload