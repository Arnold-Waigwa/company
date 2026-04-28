from django.urls import path
from . import views

app_name = "mycompany"

urlpatterns = [
    path("employee-list/", views.employee_list, name="employee_list"),
    path("employee/<int:id>/", views.employee_details, name="employee_details"),
]