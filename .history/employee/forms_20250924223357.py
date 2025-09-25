from django import forms # type: ignore
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ('emp_id','emp_name','emp_email','emp_contact')
        fields = '__all__'
        