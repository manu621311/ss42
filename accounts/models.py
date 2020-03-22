from django.db import models

# Create your models here.
from django.db import models
# from .import forms  

# Create your models here.
class signupModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
