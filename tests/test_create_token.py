from config.config import BASE_URL
from utils.payloads import auth_payload

def test_create_token(auth_token):

    response=auth_token

    assert isinstance(response,str)
    # assert data["token"] is not None
    assert len(response) > 0