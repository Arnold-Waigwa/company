from django.urls import path
from . import views

app_name = "mycompany"

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("employee/<int:id>/", views.employee_details, name="employee_details"),
    path("department-list/", views.department_list, name="department_list"),
    path("department/<int:id>/", views.department_details, name="department_details"),
    path("project-list/", views.ProjectListView.as_view(), name="project_list"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("employee-search/", views.EmployeeSearchView.as_view(), name="employee_search") 
]