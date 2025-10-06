from django.db import models
from django.conf import settings
from DjangoCRUD import settings as project_settings

class Employee(models.Model):
    emp_id = models.CharField(max_length=40)
    emp_name = models.CharField(max_length=25)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=11)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    emp_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    emp_profile = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employees", null=True, blank=True)

    @property
    def profile_url(self):
        if self.emp_profile and hasattr(self.emp_profile, 'url'):
            return self.emp_profile.url
        return f"{project_settings.MEDIA_URL}profiles/default.png"

    def __str__(self):
        return self.emp_name
