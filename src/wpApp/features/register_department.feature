Feature: Department Creation


  Scenario: Successful creation of a new department
    When I click on the "Enter" button for company with ID 1
    Then I should be redirected to the "company_detail" page for company with ID 1
    And I should see the company details
    When I enter "{department_name}" into the department creation form
    And I click the "Create Department" button
    Then I should see "{department_name}" in the list of departments
