from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name
