from behave import given, when, then
from django.urls import reverse

@given('there is a company with ID {company_id}')
def step_given_company_with_id(context, company_id):
    from django.contrib.auth.models import User
    from web.models import Company

    # Create a user with ID 1 if it doesn't exist
    user_id = 1
    user, created = User.objects.get_or_create(id=user_id)
    if created:
        # Set any necessary user properties
        user.username = 'testuser'
        user.save()

    # Create the company with the given ID and set the foreign key relationship to the user
    company = Company.objects.create(name="Test Company", email_com="test@company.com", num_workers=20, admin=user)
    context.company = company


@when('I navigate to the "company_detail" page with ID {company_id}')
def step_when_navigate_to_company_detail(context, company_id):
    url = reverse('company_detail', args=[company_id])
    context.response = context.browser.get(url)

@when('I enter "{department_name}" into the department creation form')
def step_when_enter_department_name(context, department_name):
    # Implement logic to fill the department name field in the department creation form
    form_data = {'department-name': department_name}
    context.response = context.browser.post(reverse('create-department', args=[context.company.id]), data=form_data)

@then('I should see "{department_name}" in the list of departments')
def step_then_see_department_in_list(context, department_name):
    response = context.browser.get(context.response.url)
    # Implement logic to check if the department name is present in the list of departments
    assert department_name in response.content.decode()
