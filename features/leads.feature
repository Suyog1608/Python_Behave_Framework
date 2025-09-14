Feature: leads

  Scenario: create lead
    Given user should be on login page
    When user enter the valid credentials
    Then user should navigate to home page
    When user click on new lead
    When user fills the mandatory fields and click save
    Then lead should be created successfully