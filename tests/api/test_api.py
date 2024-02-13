from random import random

import pytest
import requests

from utils.file import get_json_value

expected_data_list = get_json_value("../../test_data/expected_api_data.json", "expected_data")


@pytest.mark.api
def test_successful_authentication(base_url, get_auth_token):
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert "email" in response.json()[0]


@pytest.mark.api
def test_post_request_and_validate_status_code(base_url, get_auth_token):
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}", }
    response = requests.post(url, headers=headers, json=expected_data_list[0])
    assert response.status_code == 201


@pytest.mark.api
def test_parse_nested_json(base_url, get_auth_token):

    """ Verify nested json response. """

    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    response = requests.get(url, headers=headers)

    actual_data_list = response.json()
    assert response.status_code == 200

    # To verify individual item form response.
    assert expected_data_list[0]["name"] == actual_data_list[0]["name"]

    # To verify all item from response using loop.
    for actual_data in actual_data_list:
        actual_data["name"] == expected_data_list[0]["name"]
        actual_data["email"] == expected_data_list[0]["email"]
        actual_data["gender"] == expected_data_list[0]["gender"]
        actual_data["status"] == expected_data_list[0]["status"]


@pytest.mark.api
def test_delete_request_and_validate_status_code(base_url, get_auth_token):
    """
    Delete the first user from the public API v2.

    Parameters:
    - base_url (str): The base URL of the API.
    - get_auth_token (callable): A function or variable providing the authentication token.

    Raises:
    - AssertionError: If the DELETE request does not return a status code of 204.
    """

    # Get the ID of the first user
    url = f"{base_url}/public/v2/users/"
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    response = requests.get(url, headers=headers)
    user_id = response.json()[0]["id"]

    # Delete the user with the obtained ID
    url = f"{base_url}/public/v2/users/{user_id}"
    response = requests.delete(url, headers=headers)

    # Assert that the DELETE request was successful (status code 204)
    assert response.status_code == 204, f"Failed to delete user. Status code: {response.status_code}"
