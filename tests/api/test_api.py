from random import random

import pytest
import requests

from helpers.utils import get_json_value

expected_data_list = get_json_value("../test_data/expected_api_data.json", "expected_data")


@pytest.mark.api
def test_successful_authentication(base_url, get_auth_token):
    """
    Test successful authentication for accessing user data.

    Args:
        base_url (str): The base URL of the API.
        get_auth_token (str): The authentication token obtained from fixture.

    Raises:
        AssertionError: If the response status code is not 200 or if the response
            does not contain the expected key "email".

    """
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert "email" in response.json()[0], "Expected key 'email' not found in response data"


@pytest.mark.xfail
@pytest.mark.api
def test_post_request_and_validate_status_code(base_url, get_auth_token):
    """
    Test a POST request and validate the status code.

    Args:
        base_url (str): The base URL of the API.
        get_auth_token (str): The authentication token obtained from fixture.

    Raises:
        AssertionError: If the response status code is not 201.

    """
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}", }
    response = requests.post(url, headers=headers, json=expected_data_list[0])
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"


@pytest.mark.xfail
@pytest.mark.api
def test_parse_nested_json(base_url, get_auth_token):
    """
    Test parsing and verification of nested JSON response from a GET request.

    Args:
        base_url (str): The base URL of the API.
        get_auth_token (str): The authentication token obtained from fixture.

    Raises:
        AssertionError: If the response status code is not 200, or if the nested JSON structure
            does not match the expected structure.

    """
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    response = requests.get(url, headers=headers)

    # Extract the actual data from the response
    actual_data_list = response.json()

    # Verify the response status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # To verify individual item form response.
    assert expected_data_list[0]["name"] == actual_data_list[0]["name"]

    # To verify all item from response using loop.
    for actual_data in actual_data_list:
        assert actual_data["name"] == expected_data_list[0]["name"]
        assert actual_data["email"] == expected_data_list[0]["email"]
        assert actual_data["gender"] == expected_data_list[0]["gender"]
        assert actual_data["status"] == expected_data_list[0]["status"]


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
