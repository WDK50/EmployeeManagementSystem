from django.db import models # type: ignore

# Create your models here.
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
    
    emp_gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='M')
    emp_profile = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.png')
    
    @p
    for emp in Employee.objects.filter(emp_profile__isnull=True):
    emp.emp_profile = "profiles/default.png"
    emp.save()
    
    def __str__(self):
        return self.emp_name()