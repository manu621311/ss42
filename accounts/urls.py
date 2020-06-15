from .views import create_verification
from django.urls import path

urlpatterns = [
    path('create/<int:id>', create_verification)
]