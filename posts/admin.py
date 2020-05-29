from django.contrib import admin
from .models import Post, Message, Comment, Img,PostAdvertisment

# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Img)
admin.site.register(PostAdvertisment)
# admin.site.register(comments)
# admin.site.register(Rating)
