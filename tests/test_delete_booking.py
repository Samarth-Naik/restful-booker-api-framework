from config.config import BASE_URL
import requests

def test_delete_booking(auth_token,create_booking):

    headers={
        "Cookie":f"token={auth_token}"
    }
    data,_=create_booking
    booking_id=data["bookingid"]
    response=requests.delete(f"{BASE_URL}/booking/{booking_id}",headers=headers)

    assert response.status_code == 201
    assert "created" in response.text.lower()

    #verify deletion

    get_booking=requests.get(f"{BASE_URL}/booking.{booking_id}")
    assert get_booking.status_code == 404