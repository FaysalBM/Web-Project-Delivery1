Feature: Create company

  Background: There is a registered user
    Given Exists a user "testuser4" with password "@TEST131202"

  Scenario: Register just company name
    Given I login as user "testuser4" with password "@TEST131202"
    When I go to the web-home page
    And I register company
      | name        |
      | The TestCompany  |
    Then I'm viewing the details page for company by "user"
      | name        |
      | The TestCompany  |
    And There are 1 companies
