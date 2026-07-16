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
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture
def create_booking():
    payload={
    "firstname" : "Michael",
    "lastname" : "Scofield",
    "totalprice" : 222,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    response=requests.post(f"{BASE_URL}/booking",json=payload)
    assert response.status_code == 200
    return response.json(),payload