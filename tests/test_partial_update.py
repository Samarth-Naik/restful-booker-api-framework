from config.config import BASE_URL
import requests
from jsonschema import validate
from schemas.get_update_booking_schema import get_update_booking_schema
from utils.payloads import partial_update_payload
from utils.api_client import ApiClient

def test_partial_update_booking(auth_token,create_booking):

    data,original_payload=create_booking

    booking_id=data["bookingid"]

    update_payload=partial_update_payload

    headers={
        "Cookie":f"token={auth_token}"
    }

    response=ApiClient.patch(f"{BASE_URL}/booking/{booking_id}",update_payload,headers)

    print(response.json())

    assert response.status_code == 200

    updated_data=response.json()

    assert "firstname" in updated_data
    assert "lastname" in updated_data
    assert "bookingdates" in updated_data
    assert "additionalneeds" in updated_data

    assert isinstance(updated_data,dict)
    assert updated_data["firstname"] == update_payload["firstname"]
    assert updated_data["additionalneeds"] == update_payload["additionalneeds"]

    assert updated_data["lastname"] == original_payload["lastname"]
    assert updated_data["totalprice"] == original_payload["totalprice"]
    assert updated_data["depositpaid"] == original_payload["depositpaid"]
    assert updated_data["bookingdates"] == original_payload["bookingdates"]

    validate(updated_data,schema=get_update_booking_schema)