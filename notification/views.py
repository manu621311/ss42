from django.shortcuts import render
from .models import Notification
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NotificationSerializer

def home(request):
    return render(request, 'notification/index.html') #for debugging

class NotificationList(APIView):
    def get(self, request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        else:
            return HttpResponse("Please Login")
        queryset = Notification.objects.all().filter(receiver=username)
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)
