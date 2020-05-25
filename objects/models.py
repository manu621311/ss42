from django.db import models
from taggit.managers import TaggableManager



class Profile(models.Model):
    username = models.CharField(max_length=30, blank=True)
    userid=models.PositiveIntegerField(blank=True,null=True)
    tags = TaggableManager(blank=True)
    Scrapcoins = models.PositiveIntegerField(default=0)
    Licenced=models.BooleanField(default=False)
    def __str__(self):
        return self.username
