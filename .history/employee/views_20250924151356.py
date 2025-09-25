from django.shortcuts import render,redirect # type: ignore
from django.http import HttpResponse # type: ignore

from employee.forms import EmployeeForm
from employee.models import Employee # type: ignore
# Create your views here.
def Home(request):
    return HttpResponse("Welcome to Django CRUD")

# Create View
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})
# List View
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})

# Update View
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
        
        else:
            form = EmployeeForm(instance=employee)
        return render(request, 'update.html', {'form':form})
    
# Delete View
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')