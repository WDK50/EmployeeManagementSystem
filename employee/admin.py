from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'emp_email', 'emp_contact', 'emp_gender', 'is_active', 'created_by', 'created_at')
    list_filter = ('is_active', 'emp_gender', 'created_by')
    search_fields = ('emp_name', 'emp_email', 'emp_contact')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('created_by',)
        return super().get_readonly_fields(request, obj)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
