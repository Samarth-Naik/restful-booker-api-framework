import requests
from config.config import BASE_URL

def test_create_booking(create_booking):

    data,payload=create_booking

    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)

    assert "booking" in data
    assert isinstance(data["booking"], dict)

    booking=data["booking"]

    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]
    assert booking["depositpaid"] == payload["depositpaid"]
    assert booking["additionalneeds"] == payload["additionalneeds"]