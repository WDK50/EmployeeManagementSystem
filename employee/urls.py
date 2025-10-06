from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path # type: ignore
from employee.views import bulk_delete_employee, create_employee,delete_employee, export_csv, individual_employee, search_employee, send_email,update_employee,employee_list # type: ignore
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, profile, update_password

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
  path('api/', include(router.urls)),
   path('update-password/', update_password, name='update_password'),
  path("profile/", profile, name="profile"),
  path('', employee_list, name='list'),
  path('export/csv/', export_csv, name='export_csv'),
  path('search/', search_employee, name='search_employee'),
  path('create/', create_employee, name='create'),
  path('update/<int:pk>/', update_employee, name='update'),
  path('delete/<int:pk>/', delete_employee, name='delete'), 
   path("bulk-delete/", bulk_delete_employee, name="bulk_delete"),
  path('detail/<int:pk>/', individual_employee, name='detail'),
  path('send_email/<int:pk>/', send_email, name='send_email'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
