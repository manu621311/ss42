from django.contrib import admin
from .models import Post, Message, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Comment)

# admin.site.register(comments)
# admin.site.register(Rating)
