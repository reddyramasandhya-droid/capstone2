from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)