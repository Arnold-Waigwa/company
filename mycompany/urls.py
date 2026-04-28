from django.urls import path
from . import views

app_name = "mycompany"

urlpatterns = [
    path("employee-list/", views.employee_list, name="employee_list"),
    path("employee/<int:id>/", views.employee_details, name="employee_details"),
    path("department-list/", views.department_list, name="department_list"),
    path("department/<int:id>/", views.department_details, name="department_details")
]