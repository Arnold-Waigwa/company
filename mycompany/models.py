from django.db import models


class SexChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class Employee(models.Model):
    ssn = models.CharField(primary_key=True, max_length=9)

    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    birth_date = models.DateField()
    address = models.TextField()

    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,
        null=True,
        blank=True
    )

    salary = models.DecimalField(max_digits=10, decimal_places=2)

    supervisor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    department = models.ForeignKey(
        "Department",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.ssn} - {self.first_name} {self.last_name}"
    
    @property
    def as_dict(self):
        return {
            "SSN": self.ssn,
            "First Name": self.first_name,
            "Middle Initial": self.middle_initial or "N/A",
            "Last Name": self.last_name,
            "Address": self.address,
            "Birth Date": self.birth_date,
            "Sex": self.get_sex_display() if self.sex else "N/A",
            "Salary": f"${self.salary}",
            "Supervisor": f"{self.supervisor.first_name} {self.supervisor.last_name}" if self.supervisor else "None",
            "Department": self.department.department_name if self.department else "None"
        }
    
class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)
    department_number = models.CharField(primary_key=True, max_length=10)

    manager = models.ForeignKey(
        Employee,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="managed_departments",
    )

    manager_start_date = models.DateField()

class Project(models.Model):
    project_name = models.CharField(unique=True, max_length=50)
    project_number = models.IntegerField(primary_key=True)
    project_location = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.CASCADE,
    )

class WorksOn(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    hours = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "project"],
                name="unique_employee_project"
            )
        ]

class DeptLocation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["department", "location"],
                name="unique_department_location"
            )
        ]


class Dependent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    dependent_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, null=True, blank=True)
    birth_date = models.DateField()
    relationship = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "dependent_name"],
                name="unique_dependent"
            )
        ]