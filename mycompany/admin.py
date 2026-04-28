from django.contrib import admin
from .models import Employee, Department, Project, WorksOn, DeptLocation, Dependent

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(WorksOn)
admin.site.register(DeptLocation)
admin.site.register(Dependent)