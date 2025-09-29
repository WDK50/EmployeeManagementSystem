import csv
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

from django.core.paginator import Paginator

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

    # Sorting
    order = request.GET.get('order')  # e.g., "name_asc", "name_desc", "created_at_asc", "created_at_desc"
    if order == "name_asc":
        employees = employees.order_by("emp_name")
    elif order == "name_desc":
        employees = employees.order_by("-emp_name")
    elif order == "created_at_asc":
        employees = employees.order_by("created_at")
    elif order == "created_at_desc":
        employees = employees.order_by("-created_at")
        
    # pagination
    paginator = Paginator(employees, 5, orphans=2)  # 10 employees per page
    page_number = request.GET.get('page')
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
    
def bulk_delete_employee(request):
    ids = request.POST.get("ids")  # This comes from the hidden input in the modal
    if ids:
        id_list = ids.split(",")  # Convert comma-separated string to list
        employees = Employee.objects.filter(id__in=id_list)
        count = employees.count()
        employees.delete()
        messages.success(request, f"{count} employee(s) deleted successfully.")
    else:
        messages.warning(request, "No employees selected for deletion.")
    return redirect("list")


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email', 'Contact', 'Gender', 'Status', 'Created At'])

    employees = Employee.objects.all()

    for emp in employees:
        writer.writerow([
            emp.emp_id,
            emp.emp_name,
            emp.emp_email,
            emp.emp_contact,
            emp.emp_gender,
            emp.emp_profile,
            emp.created_at.strftime('%Y-%m-%d')
        ])

    return response
