from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.home, name='web-home'),
    path('about/',views.about, name='web-about'),
    path('create_project/', views.create_project, name='create_project'),
    path('register/', views.registerPage, name='register_user'),
    path('login/', views.loginPage, name='login_user'),
    path('logout/', views.logoutPage, name='logout_user'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('add_task/<int:project_id>/', views.add_task, name='add-task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete-task'),
    path('departments/<int:department_id>/create_project/', views.create_project, name='create-project'),
]
