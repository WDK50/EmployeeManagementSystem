from django import forms # type: ignore
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ('emp_id','emp_name','emp_email','emp_contact')
        fields = '__all__'
        exclude = ['created_by']
        labels = {
            'emp_id': 'Employee ID',
            'emp_name': 'Full Name',
            'emp_email': 'Email Address',
            'emp_contact': 'Contact Number',
            'emp_gender': 'Gender',
            'emp_profile': 'Profile Picture',
        }