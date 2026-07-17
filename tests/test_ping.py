import requests
from config.config import BASE_URL
from utils.api_client import ApiClient

def test_health_check():
    response=ApiClient.get(f"{BASE_URL}/ping")

    print(response)
    assert response.status_code == 201
