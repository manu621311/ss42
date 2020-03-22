from django.db import models
import uuid # new

from django.db import models # new
from django.shortcuts import reverse # new
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title=models.CharField(max_length=128,null=True,blank=True)
    rate=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],default=True,null=True,blank=True)

    # rating=models.IntegerField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    review=models.CharField(max_length=250,null=True,blank=True)
    url=models.URLField(null=True,blank=True)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="post_voters")
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.content}'
    def get_absolute_url(self):
        return reverse('post:post_detail' , kwargs={'post_id':post.id})
    # def no_of_rating(self):
    #     ratings=Rating.objects.filter(Post=self)
    #     return len(ratings)
    # def avg_rating(self):
    #     sum = 0
    #     ratings = Rating.objects.filter(Post=self)
    #     for rating in ratings:
    #         sum += rating.stars
    #
    #     if len(ratings) > 0:
    #         return sum / len(ratings)
    #     else:
    #         return 0

# class Rating(models.Model):
#     Post=models.ForeignKey(Post,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
#     class Meta:
#         unique_together =(( 'user' ,'Post'),)
#         index_together =(( 'user' ,'Post'),)

# class comments(models.Model):
#     # created_at=models.DateTimeField(auto_now_add=True)
#     content=models.CharField(max_length=128,default=True)
#     post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments",default=True)
#     author=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,default=True,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.author.username
