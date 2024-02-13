import pytest
import requests

@pytest.fixture
def base_url():
    return "https://gorest.co.in"

@pytest.fixture
def get_auth_token():
    token = "5b4a8f46b8d818ff3df02f3100df34e5b2af8e83be151d77e40f1e28abd24821"
    return token

@pytest.fixture
def clear_inbound_test_data_from_hubspot_before_and_after_the_test():
    yield

    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}", }

    response = requests.delete(url, headers=headers)
    assert response.status_code == 201