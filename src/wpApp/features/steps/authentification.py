from behave import given, when, then
from django.test import Client
from django.urls import reverse

@given('I navigate to the "{page}" page')
def step_nav_to_page(context, page):
    context.browser = Client()
    context.response = context.browser.get(reverse(page))

@when('I enter the following details into the registration form')
def step_enter_registration_details(context):
    for row in context.table:
        context.registration_details = {
            'username': row['username'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password1': row['password1'],
            'password2': row['password2'],
        }

@when('I click the "{button_name}" button')
def step_click_button(context, button_name):
    if button_name == 'Register Account':
        context.response = context.browser.post(reverse('register_user'), context.registration_details)
    elif button_name == 'Login':
        context.response = context.browser.post(reverse('login_user'), context.login_details)

@then('I should be redirected to the "{page}" page')
def step_redirect_to_page(context, page):
    assert context.response.status_code == 302
    assert context.response.url == reverse(page)

@when('I enter the following details into the login form')
def step_enter_login_details(context):
    for row in context.table:
        context.login_details = {
            'username': row['username'],
            'password': row['password'],
        }

@then('I should see a welcome message')
def step_see_welcome_message(context):
    response = context.browser.get(context.response.url)
    assert 'Welcome' in response.content.decode()
