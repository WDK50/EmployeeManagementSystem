from django.urls import path # type: ignore
from employee.views import create_employee,delete_employee,update_employee,employee_list # type: ignore

urlpatterns = [
  path('', employee_list, name='list'),
  path('create/', create_employee, name='create'),
  path('update/<int:pk>/', update_employee, name='update'),
  path('delete/<int:pk>/', delete_employee, name='delete'),    
]
