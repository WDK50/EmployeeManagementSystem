from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=40)
    emp_name = models.CharField(max_length=25)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=11)
    emp_gender = models
    
    def __str__(self):
        return self.emp_name()