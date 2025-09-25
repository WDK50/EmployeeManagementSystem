from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from employee.forms import EmployeeForm
from employee.models import Employee 
from .models import Employee


# Create your views here.
def send_email(request,pk):
     employee = get_object_or_404(Employee, pk=pk)
     subject = "Company Welcome"
     message = f"Congrats {employee.emp_name},\n\nWelcome to the company! We are excited to have you on board.\n\nBest regards,\nCompany Team"
     recipient = [employee.emp_email]
     send_mail(subject, message, 'ka479690@gmail.com', recipient)
     
     messages.success(request, f"Email sent successfully to {employee.emp_email}")
     return redirect('list')
    
    
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
    employees = Employee.objects.all().order_by("id")   # sort by id or name
    paginator = Paginator(employees, )  # 5 employees per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

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