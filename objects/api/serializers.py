from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post
from objects.models import Profile
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)



class UserDetailSerializer(serializers.ModelSerializer):
    """for all  getting all objects of a particular user """
    tags = TagListSerializerField()
    author=serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','title','rate','author','content','review','url','tags')

class ProfileSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    username = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'tags')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
