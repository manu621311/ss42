from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import UserDetailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import mixins
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response


# class UserView(mixins.RetrieveModelMixin, APIView):
#     """ this is to get the  all the objects created by a  indiviual user through id"""
#     serializer_class= UserDetailSerializer
#     permission_classes=[AllowAny]
#     lookup_field='id'
#     def get_queryset(self, *args, **kwargs):
#         if self.kwargs['id']:
#             return User.objects.all().filter(id=self.kwargs['id'])


#@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_current_user(request):
#     serializer = UserDetailSerializer(request.user)
#     return Response(serializer.data)


class userView(mixins.RetrieveModelMixin, APIView):
    """ this is to get the  all the objects created by a  indiviual user through id"""
    serializer_class = UserDetailSerializer
    model = User
    lookup_field='id'
    @permission_classes([IsAuthenticated, IsAdminUser])
    @api_view(['GET'])
    def get_queryset(self, *args, **kwargs):
        if self.kwargs['id']:
            return User.objects.all().filter(user=self.kwargs['id'])