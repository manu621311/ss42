
# from django_registration.backends.one_step.views import RegistrationView
# from django_registration.backends.one_step import RegistrationView
# from django_registration.backends.one_step.views import RegistrationView

# from django_registration.one_step.views import RegistrationView
# from users.forms import CustomUserForm
from objects.api import views
from django.urls import path,include,re_path
from django.conf.urls import url

from posts.models import Post, Comment, Message, Img

from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()

router.register(r'post', views.ProfilePostViewSet, Post)               # Route for profile post view
router.register(r'message', views.ProfileMsgViewSet, Message)
router.register(r'img', views.ProfileImgViewSet, Img)


urlpatterns = [

    path('',  include(router.urls)),

    url('^me/$', views.PostListUser.as_view()),
    path('profile/', views.ProfileTags.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
    path('all/img', views.UserImgProfile.as_view({'get': 'list'})),
    path('all/msg', views.UserMsgProfile.as_view({'get': 'list'})),
    path('all/post', views.UserPostProfile.as_view({'get': 'list'})),

    # path('post/', views.ProfilePostViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),



    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^.*$',IndexTemplateView.as_view(),name='entry point')





]
