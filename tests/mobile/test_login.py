import time
import pytest
from pytest_bdd import scenario, given, when, then

from helpers.appium_driver import find_element_by_accessibility_id, swipe_to_element_by_accessibility_id
from helpers.utils import get_json_value


credentials = get_json_value("../../test_credentials/credentials.json", "test_user1")


@pytest.mark.mobile
@scenario("../../feature/login.feature", "Successful Login")
def test_successful_login():
    """
    Test for the Successful Login scenario.

    Parameters:
    - appium_driver: Appium WebDriver instance.
    """


@pytest.mark.mobile
@scenario("../../feature/login.feature", 'Unsuccessful Login - Empty credentials')
def test_unsuccessful_login_empty_credentials():
    """
        Test for the Unsuccessful Login scenario.
        Note: This test is expected to fail.

        Parameters:
        - appium_driver: Appium WebDriver instance.
    """


@given('User is on the login page')
def user_is_on_the_login_page():
    # App launched and User is on the login page.
    # Assuming the login page is already open
    pass


@when('User enters valid username and password')
def user_enters_valid_username_and_password(appium_driver):
    # User enters valid username and password
    find_element_by_accessibility_id(appium_driver, "Username").send_keys(credentials['username'])
    find_element_by_accessibility_id(appium_driver, "Password").send_keys(credentials['password'])


@when('User swipe down and clicks the login button')
def user_swipe_down_and_clicks_the_login_button(appium_driver):
    # User swipe to element
    swipe_to_element_by_accessibility_id(appium_driver, 'Login', 10, 20)

    # User clicks the login button
    find_element_by_accessibility_id(appium_driver, "Login").click()


@then('User should see Welcome message')
def user_should_see_welcome_message(appium_driver):
    # User should see Welcome to Banking message
    # Get the text from the element to assert
    time.sleep(10)
    element = find_element_by_accessibility_id(appium_driver, "Welcome to Banking")
    element_text = element.text
    assert "Welcome to Banking" == element_text, "Could not find 'Welcome' text on the page."
    pass


@when('User enters empty username and password')
def user_enters_empty_username_and_password(appium_driver):
    # User enters empty username and password
    find_element_by_accessibility_id(appium_driver, 'Username').send_keys('')
    find_element_by_accessibility_id(appium_driver, 'Password').send_keys('')
    pass


@then('User should remain on the login page')
def user_should_remain_on_the_login_page(appium_driver):
    # User shouldn't see Welcome message
    # Get the text from the element to assert
    element = find_element_by_accessibility_id(appium_driver, "Welcome to Banking")
    element_text = element.text
    assert "Login" == element_text, "Could not find 'Login' text on the page."

    # This assertion should fail as login expected to be unsuccessful.
    assert "Welcome to Banking" == element_text, "Could not find 'Welcome' text on the page."
