from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
User = get_user_model()

class Task(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=256)
    tasks = models.ManyToManyField(Task)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
    
    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=256)
    projects = models.ManyToManyField(Project)
    num_projects = models.IntegerField(default=0)
    users = models.ManyToManyField(User)
    num_users = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=256)
    email_com = models.EmailField(max_length=255, unique=True, default='defaultEmail')
    num_workers = models.IntegerField(default=0)
    departments = models.ManyToManyField(Department)
    workers = models.ManyToManyField(User)
    def __unicode__(self):
        return self.name
    

"""
class User(AbstractBaseUser):
    id_user = models.CharField(max_length=255, primary_key=True)
    email_user = models.EmailField(max_length=255, unique=True, default='defaultUserMail')
    name = models.CharField(max_length=255)
    profile_photo = models.BinaryField(null=True, blank=True)
    projects = models.ManyToManyField(Project, related_name='projects', blank=True)
    groups_number = models.IntegerField()
    groups = models.ManyToManyField(Department, related_name='departments', blank=True)
    company = models.ManyToOneRel(Company, field_name='company', to='Company')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
"""
