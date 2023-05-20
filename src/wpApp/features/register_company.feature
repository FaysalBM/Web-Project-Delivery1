Feature: Create company

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just company name
    Given I login as user "user" with password "password"
    When I go to the web-home page
    And I register company
      | name        |
      | The TestCompany  |
    Then I'm viewing the details page for company by "user"
      | name        |
      | The TestCompany  |
    And There are 1 companies
