Feature: login

Scenario: valid login
Given user should be on login page
When user enter the valid credentials
Then user should navigate to home page


Scenario: invalid login
Given user should be on login page
When user enter the invalid credentials
Then user should see the error message