# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('', admin.site.urls),
# ]
from django.urls import include, path
from rest_framework import routers
from posts.api import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter,DefaultRouter

from posts.models import Post, Comment


from posts.api  import views
router = DefaultRouter()

router.register(r'post', views.PostViewSet)
router.register(r'msg', views.MsgViewSet)
router.register(r'comments', views.CommentViewSet, Comment)
router.register(r'tagg', views.FakeViewSet, Post)
# router.register(r'ratings', views.RatingViewSet)
# router.register(r'users', views.UserViewSet)


# router.register(r'users', views.UserViewSet)
# router = routers.DefaultRouter()
# router.register('list', views.Postsnippet)
# router.register()
# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('list/(?P<id>[0-9]+)/$', views.Postsnippet.as_view(),name='post_list'),
    path('',  include(router.urls)),
    # path('post/<slug:id>/comment',views.CommentsCreateAPIView.as_view(),name="comment"),
    path('post/<slug:id>/detail',views.PostRUDView.as_view(),name="detail"),
    path('post/<int:pk>/like',views.PostLikeView.as_view(),name="like"),
    # url(r'^nice/(?P<id>\d+)$',userView.as_view(),name='username'),


    # path('get',views.api_get_create,name='get_test'),
    # path('update/<int:pk>/',views.api_delete,name='put_test')



]
