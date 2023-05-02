from django import forms
from django.contrib.auth.forms import UserCreationForm
from web.models import Project
from web.models import Company

class ProjectForm(UserCreationForm):

    class Meta:
        model = Project
        fields = ['name', 'tasks']

