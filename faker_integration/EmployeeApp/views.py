from django.shortcuts import render
from .models import *
# Create your views here.
def display_emp(request):
    objs = Employee.objects.all()
    template_name = 'EmployeeApp/display.html'
    context = {'employees':objs}
    return render(request,template_name,context)

