from .views import PostList
from django.urls import path,include,re_path
from django.conf.urls import url



urlpatterns = [
    url('^(?P<id>.+)/$', PostList.as_view()),
]