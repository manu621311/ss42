from .views import get_current_user
from django.urls import path,include,re_path
from django.conf.urls import url



urlpatterns = [
    path('', get_current_user, name='userDetails'),
    #re_path(r'(?P<id>[0-9]+)$', UserView.as_view(), name='userDetails'),
]