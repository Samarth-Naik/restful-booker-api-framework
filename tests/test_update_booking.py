from config.config import BASE_URL
import requests

def test_update_booking(auth_token,create_booking):

    data,_=create_booking

    booking_id=data["bookingid"]

    update_payload={
    "firstname" : "Michael-updated",
    "lastname" : "Scofield-updated",
    "totalprice" : 555,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-02-02",
        "checkout" : "2019-02-02"
    },
    "additionalneeds" : "Lunch"
    }

    headers={
        "Cookie":f"token={auth_token}"
    }

    response=requests.put(f"{BASE_URL}/booking/{booking_id}",json=update_payload,headers=headers)

    print(response.json())

    assert response.status_code == 200

    updated_data=response.json()

    assert "firstname" in updated_data
    assert "lastname" in updated_data
    assert "bookingdates" in updated_data
    assert "additionalneeds" in updated_data

    assert isinstance(updated_data,dict)
    assert updated_data["firstname"] == update_payload["firstname"]
    assert updated_data["lastname"] == update_payload["lastname"]
    assert updated_data["totalprice"] == update_payload["totalprice"]
    assert updated_data["depositpaid"] == update_payload["depositpaid"]
    assert updated_data["additionalneeds"] == update_payload["additionalneeds"]
    assert updated_data["bookingdates"]["checkin"] == update_payload["bookingdates"]["checkin"]
    assert updated_data["bookingdates"]["checkout"] == update_payload["bookingdates"]["checkout"]