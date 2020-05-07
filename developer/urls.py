from django.urls import path
from .views import SaveToken
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', csrf_exempt(SaveToken.as_view())),
]