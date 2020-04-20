from rest_framework import serializers

from notification.models import Notification
from django.contrib.auth.models import User
from posts.models import Post


class NotificationSerializer(serializers.ModelSerializer):
    post = serializers.RelatedField(source='Post', read_only=True)
    receiver = serializers.RelatedField(source='User', read_only=True)
    sender = serializers.RelatedField(source='User', read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'
