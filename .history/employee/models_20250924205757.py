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
    emp_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    ]
    def __str__(self):
        return self.emp_name()