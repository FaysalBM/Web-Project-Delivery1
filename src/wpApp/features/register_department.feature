Feature: Department Creation

  Scenario: Successful creation of a new department
    Given I navigate to the "company_detail" page
    When I enter "{department_name}" into the department creation form
    And I click the "Create Department" button
    Then I should see "{department_name}" in the list of departments
