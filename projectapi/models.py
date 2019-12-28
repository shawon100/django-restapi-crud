from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_code=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)