from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse 
from django.core.mail import send_mail
from employee.forms import EmployeeForm
from employee.models import Employee 

# Create your views here.
def send_email(request,pk):
     employee = get_object_or_404(Employee, pk=pk)
     subject = "Welcome from Company"
    
    
    
    
# Create View
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})

def individual_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    return render(request, 'detail.html', {'employee': employee})

# List View
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})

# Update View
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES, instance=employee )

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
