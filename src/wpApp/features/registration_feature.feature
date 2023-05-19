Feature: User Registration

  Scenario: Successful registration and login
    Given I navigate to the "register_user" page
    When I enter the following details into the registration form
      | username  | first_name | last_name | email | password1  | password2 |
      | testuser4 | Test | User2 | test@user.com | @TEST131202 | @TEST131202 |
    And I click the "Register Account" button
    Then I should be redirected to the "login_user" page
    When I enter the following details into the login form
      | username  | password  |
      | testuser4  | @TEST131202  |
    And I click the "Login" button
    Then I should be redirected to the "web-home" page
