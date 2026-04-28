from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee

# Create your views here.
#request comes in like GET /Employee-list
def employee_list(request):
    #fetch all employee
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employee_list": employees})

def employee_details(request, id):
    #takes in id(ssn primary key) from url, 404 will handle 404
    employee = get_object_or_404(Employee, ssn=id)
    return render(request, "employee/employee_detail.html", {"employee": employee})

        

