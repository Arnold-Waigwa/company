from django.db import models
import datetime


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
        on_delete=models.SET_NULL,
        related_name="employees"
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
            "Department": self.department.department_name if self.department else "None",
            "Projects": [
                    {
                      "name": work.project.project_name,
                      "number": work.project.project_number,
                      "hours": work.hours
                    }
                    for work in self.works_on.all()
                ],
            "Dependents": [
                {
                  "name": dep.dependent_name,
                  "relationship": dep.relationship,
                  "birth_date": dep.birth_date,
                  "sex": dep.get_sex_display() if dep.sex else "N/A"
                }
                for dep in self.dependents.all()
            ]
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

    def __str__(self):
        return f"{self.department_number}, {self.department_name}"
    
    @property
    def as_dict(self):
        return {
            "Department Name": self.department_name,
            "Department Number": self.department_number,
            "Manager": f"{self.manager.first_name} {self.manager.last_name}" if self.manager else "None",
            "Manager Start Date": self.manager_start_date if self.manager_start_date else "None",
            "Locations": ", ".join([loc.location for loc in self.locations.all()]) or "None",
            "Employees": ", ".join(f"{emp.first_name} {emp.last_name}"for emp in self.employees.all()) or "None",
            "Projects": [
                    {
                      "name": p.project_name,
                      "number": p.project_number,
                      "location": p.project_location
                    }
                    for p in self.projects.all()
                  ]
            }

class Project(models.Model):
    project_name = models.CharField(unique=True, max_length=50)
    project_number = models.IntegerField(primary_key=True)
    project_location = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    def __str__(self):
        return f"{self.project_number} - {self.project_name}"


class WorksOn(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="works_on")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="works_on")

    hours = models.FloatField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "project"],
                name="unique_employee_project"
            )
        ]
    
    def __str__(self):
        return f"{self.employee} - {self.project}"

class DeptLocation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="locations")
    location = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["department", "location"],
                name="unique_department_location"
            )
        ]
    
    def __str__(self):
        return f"{self.department} - {self.location}"


class Dependent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="dependents")

    dependent_name = models.CharField(max_length=100)
    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,
        null=True,
        blank=True
    )
    birth_date = models.DateField()
    relationship = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "dependent_name"],
                name="unique_dependent"
            )
        ]
    
    def __str__(self):
        return f"{self.dependent_name} -> Relationship : {self.relationship}"