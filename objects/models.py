from django.db import models
from taggit.managers import TaggableManager



class Profile(models.Model):
    username = models.CharField(max_length=30, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.username