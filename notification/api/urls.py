from django.urls import path

from .views import NotificationSort

urlpatterns = [
    path('sort/', NotificationSort.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
]
