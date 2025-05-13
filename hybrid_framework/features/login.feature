Feature: Login
  Scenario: Successful login
    Given the user is on the login page
    When they enter valid credentials
    Then they should see the dashboard