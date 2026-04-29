from django.shortcuts import render
from .models import Employee

def search_employee(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Employee.objects.filter(fname__icontains=query)

    return render(request, 'search.html', {'results': results})
