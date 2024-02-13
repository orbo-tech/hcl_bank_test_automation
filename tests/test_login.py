
from utils.file import get_json_value
from pytest_bdd import scenario, given, when, then

data = get_json_value("../test_data/credentials.json", "credentials")


@scenario("../features/login.feature", "Successful Login")
def test_successful_login():
    pass

@given('User is on the login page')
def user_is_on_the_login_page():
    print("Given: User is on the login page")


@when('User enters valid username and password')
def user_enters_valid_username_and_password():
    print("When: User enters valid username and password")


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

# Then steps
@then('User should see an error message "username is empty"')
def user_should_see_an_error_message_empty_username():
    print("Then: User should see an error message 'username is empty'")

@then('User should remain on the login page')
def user_should_remain_on_the_login_page():
    print("And: User should remain on the login page")

@scenario('../features/login.feature', 'Unsuccessful Login - Invalid Username')
def test_unsuccessful_login_invalid_username():
    pass

# Given step
@given('User is on the login page')
def user_is_on_the_login_page():
    print("Given: User is on the login page")

# When steps
@when('User enters invalid username and valid password')
def user_enters_invalid_username_and_valid_password():
    print("When: User enters invalid username and valid password")

@when('User clicks the login button')
def user_clicks_the_login_button():
    print("And: User clicks the login button")

# Then steps
@then('User should see an error message indicating invalid username')
def user_should_see_an_error_message_indicating_invalid_username():
    print("Then: User should see an error message indicating invalid username")

@then('User should remain on the login page')
def user_should_remain_on_login_page():
    print("And: User should remain on the login page")