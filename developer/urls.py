from django.urls import path
from .views import SaveToken

urlpatterns = [
    path('register/', SaveToken.as_view()),
]