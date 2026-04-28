from django.shortcuts import render, get_object_or_404
from .models import Employee, Department, Project
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
#request comes in like GET /Employee-list
def employee_list(request):
    #fetch all employee
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employee_list" : employees})

def employee_details(request, id):
    #takes in id(ssn primary key) from url, 404 will handle 404
    employee = get_object_or_404(Employee, ssn=id)
    return render(request, "employee/employee_details.html", {"employee" : employee})

def department_list(request):
    #show list of departments
    departments = Department.objects.all()
    return render(request, "department/department_list.html", {"department_list" : departments})

def department_details(request, id):
    department = get_object_or_404(Department, department_number=id)
    return render(request, "department/department_details.html", {"department" : department})

class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_details.html"
    context_object_name = "project"

class EmployeeSearchView(ListView):
    model = Employee
    template_name = "employee/employee_search.html"
    context_object_name = "employees"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Employee.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(ssn__icontains=query)
            )
        return Employee.objects.none()