from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

User  = get_user_model()


class Profile(models.Model):
    username = models.CharField(max_length=30, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.username
