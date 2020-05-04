from rest_framework import serializers
from posts.models import Post,Message,Comment,Img
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

#########
# class Suser(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('id','username','password')
#         extra_kwargs={'password':{'write_only':True,'required':True}}
#     def create(self,validated_data):
#         user=User.objects.create(**validated_data)
#         return user
#
# class Scomments(serializers.ModelSerializer):
#     comments_count=serializers.SerializerMethodField(read_only=True)
#     user_has_commented=serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model=comments
#         fields = '__all__'
#     def get_comments_count(self,instance):
#         return instance.comments.count()
#     def get_user_has_voted(self,instance):
#         request=self.context.get("request")
#         return instance.commentss.filter(pk=request.user.pk).exists()
class UserDetailSerializer(serializers.ModelSerializer):
    """for all  getting all objectws of a particular user """
    class Meta:
        model=Post
        fields=['id',
                'author',
                'review',
                ]

class ImgSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = serializers.StringRelatedField(read_only=True)
    # post   = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Img
        fields='__all__'
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post   = serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields='__all__'

class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = ('id','title','rate','author','content','review','url','tags', 'comments', 'created_at')
    def get_likes_count(self,instance):
        return instance.voters.count()
    def get_user_has_voted(self,instance):
        request=self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

class Spost(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()

    author=serializers.StringRelatedField(read_only=True)
    # comments= CommentSerializer(read_only=True)
    # likes_count=serializers.SerializerMethodField(read_only=True)
    # user_has_voted=serializers.SerializerMethodField(read_only=True)
    ## for string related field without displaying it as numerics , it displays the direct object of that object"
    # user=Scomments()
    class Meta:
        model = Post
        fields = ('id','title','rate','author','content','review','url','tags','comments')
    def get_likes_count(self,instance):
        return instance.voters.count()
    def get_user_has_voted(self,instance):
        request=self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

class Smessage(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author=serializers.StringRelatedField(read_only=True)
    # likes_count=serializers.SerializerMethodField(read_only=True)
    # user_has_voted=serializers.SerializerMethodField(read_only=True)
    ## for string related field without displaying it as numerics , it displays the direct object of that object"
    # user=Scomments()
    class Meta:
        model = Message
        fields = ('id','title','rate','author','content','review', 'created_at', 'tags')
    def get_likes_count(self,instance):
        return instance.voters.count()
    def get_user_has_voted(self,instance):
        request=self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()
# class Srating(serializers.ModelSerializer):
#     class Meta:
#         model=Rating
#         fields='__all__'
