import requests
from config.config import BASE_URL

def test_health_check():
    response=requests.get(f"{BASE_URL}/ping")

    print(response)
    assert response.status_code == 201
