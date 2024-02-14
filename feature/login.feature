Feature: Login Functionality

  Scenario: Successful Login
    Given User is on the login page
    When User enters valid username and password
    And User swipe down and clicks the login button
    Then User should see Welcome message

  Scenario: Unsuccessful Login - Empty credentials
    Given User is on the login page
    When User enters empty username and password
    And User swipe down and clicks the login button
    Then User should remain on the login page
