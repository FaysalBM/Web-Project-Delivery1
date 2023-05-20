from splinter import Browser
from behave import given, when, then
from django.urls import reverse
from web.models import Company

@given('there is a company with ID {company_id}')
def step_given_company_with_id(context, company_id):
    company = Company.objects.create(id=company_id)
    company.workers.add(context.user)

@when('I click on the "Enter" button for company with ID {company_id}')
def step_click_enter_button(context, company_id):
    url = reverse('company_detail', args=[company_id])
    context.response = context.browser.visit(url)

@then('I should be redirected to the "company_detail" page for company with ID {company_id}')
def step_check_redirected_to_company_detail(context, company_id):
    expected_url = reverse('company_detail', args=[company_id])
    assert context.browser.url == expected_url, f"Expected URL: {expected_url}, Actual URL: {context.browser.url}"

@then('I should see the company details')
def step_check_company_details(context):
    company = context.company
    assert company.name in context.browser.html, f"Company name '{company.name}' not found in the page"
    assert company.email_com in context.browser.html, f"Company email '{company.email_com}' not found in the page"

@when('I enter "{department_name}" into the department creation form')
def step_when_enter_department_name(context, department_name):
    form_data = {'department-name': department_name}
    context.response = context.browser.post(reverse('create-department', args=[context.company.id]), data=form_data)

@then('I should see "{department_name}" in the list of departments')
def step_then_see_department_in_list(context, department_name):
    response = context.browser.get(context.response.url)
    assert department_name in response.content.decode()
