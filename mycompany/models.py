from django.db import models

# Create your models here.
class Employee(models.Model):
    Fname = models.TextField()
    Minit = models.TextField()
    Lname = models.TextField()
    Ssn = models.CharField(primary_key=True, max_length=9)
    Bdate = models.DateField()
    Address = models.TextField()
    Sex = models.CharField(max_length=1, null=True)
    Salary = models.FloatField()
    Super_ssn = models.CharField(max_length=9)
    Dno = models.CharField()

class Department:
    Dname = models.TextField()
    Dnumber = models.CharField(primary_key=True)
    Mgr_ssn = models.CharField()
    

