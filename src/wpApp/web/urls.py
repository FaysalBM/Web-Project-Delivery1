from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.home, name='web-home'),
    path('about/',views.about, name='web-about'),
    path('create_project/', views.create_project, name='create_project'),
]
