from config.config import BASE_URL
from utils.api_client import ApiClient

def test_get_bookings():
    response=ApiClient.get(f"{BASE_URL}/booking")

    assert response.status_code == 200

    data=response.json()

    assert isinstance(data,list)
    assert len(data)>0