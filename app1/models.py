from django.db import models

# Create your models here.

class  Profile(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=50)
    summary=models.TextField(max_length=2000)
    degree=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    previous_work=models.TextField(max_length=2000)
    skills=models.TextField(max_length=2000)