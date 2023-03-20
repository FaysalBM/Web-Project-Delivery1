from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)

class Project(models.Model):
    name = models.CharField(max_length=256)

class Task(models.Model):
    name = models.CharField(max_length=256)

class Department(models.Model):
    name = models.CharField(max_length=256)
