from django.db import models
from django.contrib.auth.models import User


class Developers(models.Model):
    dev_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(null=False)
    ssEmail = models.EmailField(null=False)
    company = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=1024, null=False)
    token = models.TextField(max_length=1024, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dev_name