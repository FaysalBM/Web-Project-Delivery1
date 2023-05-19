Feature: Department Creation

  Background:
    Given there is a company with ID 1

  Scenario: Successful creation of a new department
    When I navigate to the "company_detail" page with ID 1
    When I enter "{department_name}" into the department creation form
    And I click the "Create Department" button
    Then I should see "{department_name}" in the list of departments
