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
]
    #path('company/', views.companyData, name='company_data'),
