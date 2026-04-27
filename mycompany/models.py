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
    Mgr_ssn = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Mgr_start_date = models.CharField()


class Dependent(models.Model):
    Essn = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Dependent_name = models.TextField()
    Sex = models.TextField()
    Bdate = models.CharField()
    Relationship = models.TextField()


class DEPT_LOCATIONS(models.Model):
    Dnumber = models.ForeignKey(Department, on_delete=models.CASCADE)
    Dlocation = models.TextField()


class PROJECT(models.Model):
    Pname = models.TextField()
    Pnumber = models.CharField(primary_key=True)
    Plocation = models.TextField()
    Dnum = models.ForeignKey(Department, on_delete=models.CASCADE)


class WORKS_ON(models.Model):
    Essn = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Pno = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
    Hours = models.FloatField()
