from django.db import models

class Department(models.Model):
    dname = models.CharField(max_length=50)
    dnumber = models.IntegerField(primary_key=True)
    mgr_ssn = models.CharField(max_length=9)
    mgr_start_date = models.DateField()

    def __str__(self):
        return self.dname


class Employee(models.Model):
    fname = models.CharField(max_length=50)
    minit = models.CharField(max_length=1, blank=True)
    lname = models.CharField(max_length=50)
    ssn = models.CharField(max_length=9, primary_key=True)
    bdate = models.DateField()
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    super_ssn = models.CharField(max_length=9, blank=True, null=True)
    dno = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname + " " + self.lname


class DeptLocation(models.Model):
    dnumber = models.ForeignKey(Department, on_delete=models.CASCADE)
    dlocation = models.CharField(max_length=50)

    def __str__(self):
        return self.dlocation


class Project(models.Model):
    pname = models.CharField(max_length=50)
    pnumber = models.IntegerField(primary_key=True)
    plocation = models.CharField(max_length=50)
    dnum = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname


class WorksOn(models.Model):
    essn = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pno = models.ForeignKey(Project, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=4, decimal_places=1)


class Dependent(models.Model):
    essn = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    bdate = models.DateField()
    relationship = models.CharField(max_length=50)
