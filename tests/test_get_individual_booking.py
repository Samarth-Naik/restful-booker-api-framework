from config.config import BASE_URL
from jsonschema import validate
from schemas.get_update_booking_schema import get_update_booking_schema
from utils.api_client import ApiClient

def test_get_individual_booking(create_booking):
    
    data,_=create_booking
    bookingid=data["bookingid"]
    response=ApiClient.get(f"{BASE_URL}/booking/{bookingid}")
    assert response.status_code == 200
    
    data=response.json()
    print(data)
    assert "firstname" in data
    assert "lastname" in data
    assert "totalprice" in data
    assert "bookingdates" in data

    assert isinstance(data["firstname"], str)
    assert isinstance(data["lastname"], str)
    assert isinstance(data["totalprice"], int)
    assert isinstance(data["depositpaid"], bool)
    assert isinstance(data["bookingdates"], dict)
    assert isinstance(data["additionalneeds"], str)

    booking_dates = data["bookingdates"]

    assert "checkin" in booking_dates
    assert "checkout" in booking_dates

    assert isinstance(booking_dates["checkin"], str)
    assert isinstance(booking_dates["checkout"], str)
    
    validate(data,schema=get_update_booking_schema)