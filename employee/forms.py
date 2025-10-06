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
        
# forms.py
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'dob', 'address', 'profile_image']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].label = 'Change Profile Picture'
