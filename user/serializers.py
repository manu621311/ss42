from rest_framework import serializers
from django.contrib.auth.models import User



class UserDetailSerializer(serializers.ModelSerializer):
    """for all  getting all objectws of a particular user """
    class Meta:
        model = User
        fields=['id', 'username', 'email', 'is_superuser', 'first_name', 'last_name']