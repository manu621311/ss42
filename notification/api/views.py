from rest_framework import viewsets
from .serializers import NotificationSerializer

from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from notification.models import Notification
from posts.models import Post
from django.contrib.auth.models import User

from rest_framework_api_key.permissions import HasAPIKey  # Permission for API Key check





class NotificationSort(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, HasAPIKey]
    authentication_classes =(JSONWebTokenAuthentication,TokenAuthentication)
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(receiver=self.request.user.id)

    def perform_create(self, serializer):
        sender_id = self.request.data.get('sender')
        receiver_id = self.request.data.get('receiver')
        post_id = self.request.data.get('post')
        serializer.save(
            receiver = User.objects.get(id=receiver_id),
            sender = User.objects.get(id=sender_id),
            post = Post.objects.get(id=post_id)
        )
