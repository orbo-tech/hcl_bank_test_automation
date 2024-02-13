import pytest
import requests


def test_successful_authentication(base_url, get_auth_token):
    url = f"{base_url}/posts"
    headers = {"Authorization": f"Bearer {get_auth_token}"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert "userId" in response.json()[0]


def test_send_request_and_validate_response(base_url, get_auth_token):
    url = f"{base_url}/comments/1"
    headers = {"Authorization": f"Bearer {get_auth_token}"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert "name" in response.json()


def test_parse_nested_json(base_url, get_auth_token):
    url = f"{base_url}/users/1"
    headers = {"Authorization": f"Bearer {get_auth_token}"}

    response = requests.get(url, headers=headers)
    user_data = response.json()

    assert response.status_code == 200
    assert "address" in user_data
    assert "geo" in user_data["address"]