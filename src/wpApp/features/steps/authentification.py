from behave import given, when, then
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

client = Client()

@given('I am on the registration page')
def step_given_on_registration_page(context):
    response = client.get(reverse('register'))  # Replace 'register' with your register view's URL name
    assert response.status_code == 200

@when('I register with the following details')
def step_when_register_with_details(context):
    for row in context.table:
        context.response = client.post(reverse('register'), {  # Replace 'register' with your register view's URL name
            'username': row['username'],
            'password1': row['password'],
            'password2': row['password'],
        })
        assert context.response.status_code == 302

@given('Exists a user "{username}" with password "{password}"')
def step_given_exists_user_with_password(context, username, password):
    User = get_user_model()
    User.objects.create_user(username=username, password=password)

@given('I am on the login page')
def step_given_on_login_page(context):
    response = client.get(reverse('login'))  # Replace 'login' with your login view's URL name
    assert response.status_code == 200

@when('I login with username "{username}" and password "{password}"')
def step_when_login_with_username_and_password(context, username, password):
    context.response = client.post(reverse('login'), {  # Replace 'login' with your login view's URL name
        'username': username,
        'password': password,
    })
    assert context.response.status_code == 302

@then('I should be redirected to the home page')
def step_then_redirected_to_home_page(context):
    assert context.response['Location'] == reverse('home')  # Replace 'home' with your home view's URL name

@then('I should be logged in as "{username}"')
def step_then_logged_in_as(context, username):
    user = get_user_model().objects.get(username=username)
    assert int(client.session['_auth_user_id']) == user.pk
