from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import UserDetailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import mixins, generics
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from posts.models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class PostList(generics.ListAPIView, APIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        """
        This view should return a list of all the Posts for
        the user as determined by the user id portion of the URL.
        """
        user_id = self.kwargs['id']
        # user = User.objects.get(id = user_id)
        return Post.objects.filter(author=user_id)