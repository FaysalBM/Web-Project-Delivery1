from behave import given, when, then
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

client = Client()

@given('Exists a user "{username}" with password "{password}"')
def step_given_exists_user_with_password(context, username, password):
    User = get_user_model()
    User.objects.create_user(username=username, password=password)

@given('I login as user "{username}" with password "{password}"')
def step_given_login_as_user_with_password(context, username, password):
    logged_in = client.login(username=username, password=password)
    assert logged_in is True

@when('I go to the web-home page')
def step_when_go_to_home_page(context):
    response = client.get(reverse('web-home'))  # Make sure 'home' is correct URL name
    assert response.status_code == 200

@when('I register company')
def step_when_register_company(context):
    for row in context.table:
        context.company_data = {
            'name': row['name'],
            'email_com': 'test@test.com',
            'num_workers': 10,
            'city': 'Test City',
            'stateOrProvince': 'Test State',
            'country': 'Test Country'
        }
        response = client.post(reverse('create_company'), context.company_data)
        assert response.status_code == 302
        context.company_url = response['Location']

@then('I\'m viewing the details page for company by "{username}"')
def step_then_viewing_details_page_for_company(context, username):
    response = client.get(context.company_url)
    assert response.status_code == 200
    for row in context.table:
        assert row['name'] in response.content.decode()

@then('There are {count} companies')
def step_then_there_are_companies(context, count):
    from web.models import Company  # Replace with your Company model import
    assert Company.objects.count() == int(count)
