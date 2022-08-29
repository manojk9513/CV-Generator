from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=200)
    summery=models.TextField(max_length=200)
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    exprience=models.TextField(max_length=200)
    skills=models.CharField(max_length=200)
    
