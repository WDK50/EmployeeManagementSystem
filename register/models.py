# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    contact = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profiles/", default="profiles/default.png")

    def __str__(self):
        return self.username
