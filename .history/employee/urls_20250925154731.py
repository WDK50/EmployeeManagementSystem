from django.urls import path # type: ignore
from employee.views import create_employee,delete_employee, individual_employee, send_email,update_employee,employee_list # type: ignore

urlpatterns = [
  path('', employee_list, name='list'),
  path('search/', search_employee, name='search_employee'),
  path('create/', create_employee, name='create'),
  path('update/<int:pk>/', update_employee, name='update'),
  path('delete/<int:pk>/', delete_employee, name='delete'), 
  path('detail/<int:pk>/', individual_employee, name='detail'),
  path('send_email/<int:pk>/', send_email, name='send_email'),   
]
