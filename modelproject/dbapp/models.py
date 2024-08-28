from django.db import models

# Create your models here.

class student(models.Model):
    studentno=models.IntegerField()
    studentname=models.CharField(max_length=30)
    studentdept=models.IntegerField()
    studentaddress=models.CharField(max_length=50)
