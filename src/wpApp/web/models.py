from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Task(models.Model):
    name = models.CharField(max_length=256)
    creator = User.get_username
    
class Project(models.Model):
    name = models.CharField(max_length=256)
    tasks = models.ManyToManyField(Task)

class Department(models.Model):
    name = models.CharField(max_length=256)
    projects = models.ManyToManyField(Project)
    users = models.ManyToManyField(User)

class Company(models.Model):
    name = models.CharField(max_length=256)
    departments = models.ManyToManyField(Department)

