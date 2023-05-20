Feature: Task Creation

  Scenario: Successful creation of a new task
    Given there is a department with ID 1
    When I navigate to the "department_detail" page with ID 1
    When I create a project with name "Sample Project"
    When I enter "{task_name}" into the task creation form
    Then I should see "{task_name}" in the list of tasks
