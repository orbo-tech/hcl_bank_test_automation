from utils.file import get_json_value
from pytest_bdd import scenario, given, when, then

data = get_json_value("../../test_data/credentials.json", "credentials")


@scenario("../features/login.feature", "Successful Login")
def test_successful_login():
    """ Verify successful login scenario."""
    pass


@given('User is on the login page')
def user_is_on_the_login_page():
    lets_sign_you_in_text = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((MobileBy.XPATH, "//*[contains(@text, 'Let\'s sign you in')]")))

    assert lets_sign_you_in_text, "Could not find 'Let's sign you in' text on the page."


@when('User enters valid username and password')
def user_enters_valid_username_and_password():
    # Locate the username input field and send keys
    username_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "username_field")))
    username_input.send_keys("valid_username")

    # Locate the password input field and send keys
    password_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "password_field")))
    password_input.send_keys("valid_password")

@when('User swipe down and clicks the login button')
def user_swipes_and_and_clicks_the_login_button():
    print("And: User swipe down and clicks the login button")


@then('User should be redirected to the dashboard')
def user_should_be_redirected_to_the_dashboard():
    print("Then: User should be redirected to the dashboard")


@then('User should see Get started message')
def user_should_see_get_started_message():
    print("And: User should see Get started message")


@scenario('../features/login.feature', 'Unsuccessful Login - Empty Username')
def test_unsuccessful_login_empty_username():
    pass


@given('User is on the login page')
def user_is_on_the_login_page():
    print("Given: User is on the login page")


@when('User enters empty username and valid password')
def user_enters_empty_username_and_valid_password():
    print("When: User enters empty username and valid password")


@when('User clicks the login button')
def user_clicks_the_login_button():
    print("And: User clicks the login button")


@then('User should see an error message "username is empty"')
def user_should_see_an_error_message_empty_username():
    print("Then: User should see an error message 'username is empty'")


@then('User should remain on the login page')
def user_should_remain_on_the_login_page():
    print("And: User should remain on the login page")


@scenario('../features/login.feature', 'Unsuccessful Login - Invalid Username')
def test_unsuccessful_login_invalid_username():
    pass


@given('User is on the login page')
def user_is_on_the_login_page():
    print("Given: User is on the login page")


@when('User enters invalid username and valid password')
def user_enters_invalid_username_and_valid_password():
    print("When: User enters invalid username and valid password")


@when('User clicks the login button')
def user_clicks_the_login_button():
    print("And: User clicks the login button")


@then('User should see an error message indicating invalid username')
def user_should_see_an_error_message_indicating_invalid_username():
    print("Then: User should see an error message indicating invalid username")


@then('User should remain on the login page')
def user_should_remain_on_login_page():
    print("And: User should remain on the login page")
