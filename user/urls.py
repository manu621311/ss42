from .views import userView
from django.urls import path,include,re_path
from django.conf.urls import url



urlpatterns = [
    path('', userView.as_view(), name='userDetails'),
    #re_path('(?P<id>[0-9]+)$', userView.as_view(), name='userDetails'),
]