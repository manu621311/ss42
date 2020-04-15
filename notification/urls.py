from django.urls import path
from .views import home, NotificationList

urlpatterns = [
    path('', home),
    path('list', NotificationList.as_view()),
]