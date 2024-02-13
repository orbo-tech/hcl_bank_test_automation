Feature: Login Functionality

  Scenario: Successful Login
    Given User is on the login page
    When User enters valid username and password
    And User swipe down and clicks the login button
    Then User should be redirected to the dashboard
    And User should see Get started message

  Scenario: Unsuccessful Login - Empty Username
    Given User is on the login page
    When User enters empty username and valid password
    And User swipe down and clicks the login button
    Then User should see an error message indicating empty username
    And User should remain on the login page
  
  Scenario: Unsuccessful Login - Invalid Username
    Given User is on the login page
    When User enters invalid username and valid password
    And User swipe down and clicks the login button
    Then User should see an error message indicating invalid username
    And User should remain on the login page
