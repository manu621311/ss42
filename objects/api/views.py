from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import UserDetailSerializer, ProfileSerializer, UserProfileSerializer
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
from objects.models import Profile
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from posts.api.permissions import IsAuthorOrReadOnly


class UserProfile(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class PostListUser(generics.ListAPIView, APIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes =(JSONWebTokenAuthentication,TokenAuthentication)

    def get_queryset(self):

        return Post.objects.filter(author=self.request.user)

class ProfileTags(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    authentication_classes =(JSONWebTokenAuthentication,TokenAuthentication)


    def get_queryset(self):
        username = self.request.user.username
        print(username)
        queryset = Profile.objects.filter(username=username)
        if queryset:
            return queryset


    def create(self, request):
        url = request.data.get('url')
        user = str(request.user)
        user_exist = Profile.objects.filter(username=self.request.user.username)
        already_exists = False
        if len(user_exist) == 0:
            already_exists = False
        else:
            already_exists = True
        if already_exists:
            return Response({"details" : "Tags for this user already exists !"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(ProfileTags, self).create(request)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Profile.objects.get(username=self.request.user.username)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(username = self.request.user.username)
