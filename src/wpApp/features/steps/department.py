from behave import given, when, then
from django.test import Client
from django.urls import reverse

@given('I navigate to the "company_detail" page')
def step_nav_to_page(context):
    context.browser = Client()
    context.response = context.browser.get(reverse('company_detail'))

@when('I enter "{department_name}" into the department creation form')
def step_enter_department_details(context, department_name):
    context.department_name = department_name

@when('I click the "Create Department" button')
def step_click_create_department(context):
    context.response = context.browser.post(reverse('create_department'), {'name': context.department_name})

@then('I should see "{department_name}" in the list of departments')
def step_see_department_in_list(context, department_name):
    response = context.browser.get(context.response.url)
    assert department_name in response.content.decode()
