from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Img, Message
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

class UserImgProfileSerializer(serializers.ModelSerializer):
    img_count = serializers.SerializerMethodField('get_img_count')
    class Meta:
        model = User
        fields = ('id', 'username', 'img_count')

    def get_img_count(self, obj):
        return Img.objects.filter(author=obj.id).count()

class UserPostProfileSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField('get_post_count')
    class Meta:
        model = User
        fields = ('id', 'username','post_count')

    def get_post_count(self, obj):
        return Post.objects.filter(author=obj.id).count()

class UserMsgProfileSerializer(serializers.ModelSerializer):
    msg_count = serializers.SerializerMethodField('get_msg_count')
    class Meta:
        model = User
        fields = ('id', 'username', 'msg_count')
    
    def get_msg_count(self, obj):
        return Message.objects.filter(author=obj.id).count()
