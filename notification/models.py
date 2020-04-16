from django.db import models
from posts.models import Post
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Notification(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True, blank=False, db_index=True)
    content=models.CharField(max_length=128,default=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="notification",default=True)
    receiver=models.ForeignKey(User ,blank=True,default=True,on_delete=models.CASCADE, related_name="receiver")
    sender=models.ForeignKey(User,blank=True,default=True,on_delete=models.CASCADE, related_name="sender")

    def __str__(self):
        return self.content