from pyexpat import model
from django.db import models

# Create your models here.

class student(models.Model):
    id= models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20,)
    
    
class Intake(models.Model):
    id= models.AutoField(primary_key=True)
    intake_name=models.CharField(max_length=100)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
