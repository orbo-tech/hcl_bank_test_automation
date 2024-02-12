Feature: Login Functionality

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters valid username and password
    And clicks the login button
    Then the user should be redirected to the dashboard
    And should see a welcome message

  Scenario: Failed Login - Invalid Username
    Given the user is on the login page
    When the user enters invalid username and valid password
    And clicks the login button
    Then the user should see an error message indicating invalid username
    And should remain on the login page
