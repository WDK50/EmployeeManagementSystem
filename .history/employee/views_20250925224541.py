from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, JsonResponse 
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
    
# Search View
def search_employee(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.filter(emp_name__icontains=query) if query else Employee.objects.all()
    
    data = []
    for emp in employees:
        data.append({
            "id": emp.id,
            "emp_id": emp.emp_id,
            "name": emp.emp_name,
            "email": emp.emp_email,
            "contact": emp.emp_contact,
            "gender": emp.get_emp_gender_display(),
            "profile": emp.emp_profile.url if emp.emp_profile else None,
        })
    
    return JsonResponse({"employees": data})

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
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
 
    status = request.GET.get('status')
    gender = request.GET.get('gender')
    created_at = request.GET.get('created_at')

    if status in ['active', 'inactive']:
        employees = employees.filter(is_active=(status == 'active'))

    if gender in ['M', 'F', 'O']:
        employees = employees.filter(emp_gender=gender)

    if created_at:
        employees = employees.filter(created_at__date=created_at)

    return render(request, "list.html", {"page_obj": employees})

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