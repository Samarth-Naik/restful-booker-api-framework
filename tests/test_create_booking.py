import requests
from config.config import BASE_URL

def test_create_booking():
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
    data=response.json()

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