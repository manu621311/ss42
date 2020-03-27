from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)



class UserDetailSerializer(serializers.ModelSerializer):
    """for all  getting all objects of a particular user """
    tags = TagListSerializerField()
    author=serializers.StringRelatedField(read_only=True)
    # likes_count=serializers.SerializerMethodField(read_only=True)
    # user_has_voted=serializers.SerializerMethodField(read_only=True)
    ## for string related field without displaying it as numerics , it displays the direct object of that object"
    # user=Scomments()
    class Meta:
        model = Post
        fields = ('id','title','rate','author','content','review','url','tags')