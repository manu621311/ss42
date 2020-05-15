from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Img, Message, Comment
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
    tags = TagListSerializerField(required=False)
    username = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'tags', 'Scrapcoins','Licenced')

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


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post   = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields='__all__'

class PostSerializer_read(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = serializers.SerializerMethodField(method_name='get_user_type')
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = ('id','title','rate','author','content','review','url','fake','tags','comments', 'created_at')
    def get_user_type(self, instance):
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.author.username
    def get_likes_count(self,instance):
        return instance.voters.count()
    def get_user_has_voted(self,instance):
        request=self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class ImgSerializer_read(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = serializers.SerializerMethodField(method_name='get_user_type')
    class Meta:
        model=Img
        fields = ('id', 'author','picture', 'created_at', 'tags', 'fake')
    def get_user_type(self, instance):
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.author.username

class MsgSerializer_read(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = serializers.SerializerMethodField(method_name='get_user_type')
    # likes_count=serializers.SerializerMethodField(read_only=True)
    # user_has_voted=serializers.SerializerMethodField(read_only=True)
    ## for string related field without displaying it as numerics , it displays the direct object of that object"
    # user=Scomments()
    class Meta:
        model = Message
        fields = ('id','title','rate','author','content','review', 'created_at', 'tags', 'fake')

    def get_user_type(self, instance):
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.author.username

    def get_likes_count(self,instance):
        return instance.voters.count()
    def get_user_has_voted(self,instance):
        request=self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()
