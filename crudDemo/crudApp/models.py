from django.db import models

class Employee(models.Model):
    eNo = models.IntegerField()
    eName = models.CharField(max_length=50)
    eSalary = models.FloatField()
    eAddress = models.CharField(max_length=100)
