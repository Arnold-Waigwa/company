from django.contrib import admin
from .models import Department, Employee, Project, WorksOn, Dependent

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(WorksOn)
admin.site.register(Dependent)
