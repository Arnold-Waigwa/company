from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Department

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