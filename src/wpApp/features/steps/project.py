from behave import given, when, then
from django.urls import reverse
from web.models import Department, Project, Task, User

@given('there is a department with ID {department_id}')
def step_given_department_with_id(context, department_id):
    context.user = User.objects.create(username='user')
    department = Department.objects.create(name="department_name", admin=context.user)
    department.admin = context.user
    department.save()
    context.department = department

@when('I navigate to the "department_detail" page with ID {department_id}')
def step_when_navigate_to_department_detail(context, department_id):
    url = reverse('department_detail', args=[1,department_id])
    context.response = context.browser.visit(url)

@when('I create a project with name "{project_name}"')
def step_when_create_project(context, project_name):
    project = Project.objects.create(name=project_name, department=context.department)
    context.project = project

@when('I enter "{task_name}" into the task creation form')
def step_when_enter_task_name(context, task_name):
    # Implement logic to fill the task name field in the task creation form
    form_data = {'task-name': task_name}
    context.response = context.browser.post(reverse('add-task', args=[context.project.id]), data=form_data)

@then('I should see "{task_name}" in the list of tasks')
def step_then_see_task_in_list(context, task_name):
    response = context.browser.get(context.response.url)
    # Implement logic to check if the task name is present in the list of tasks
    assert task_name in response.content.decode()
