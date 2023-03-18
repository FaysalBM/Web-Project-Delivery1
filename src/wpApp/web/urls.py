from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='webProject Name'),
    path('about/',views.about, name='About Us'),
]
