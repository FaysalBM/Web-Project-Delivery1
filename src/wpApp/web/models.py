from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)
    id = models.IntegerField

class Project(models.Model):
    name = models.CharField(max_length=256)
    id = models.IntegerField

class Task(models.Model):
    name = models.CharField(max_length=256)
    id = models.IntegerField