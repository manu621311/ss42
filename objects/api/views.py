from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import UserDetailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework import mixins, generics
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from posts.models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from rest_framework import viewsets


class PostListUser(generics.ListAPIView, APIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes =(JSONWebTokenAuthentication,TokenAuthentication)

    def get_queryset(self):

        return Post.objects.filter(author=self.request.user)
