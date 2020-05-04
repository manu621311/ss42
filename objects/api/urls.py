
# from django_registration.backends.one_step.views import RegistrationView
# from django_registration.backends.one_step import RegistrationView
# from django_registration.backends.one_step.views import RegistrationView

# from django_registration.one_step.views import RegistrationView
# from users.forms import CustomUserForm
from objects.api import views
from django.urls import path,include,re_path
from django.conf.urls import url

urlpatterns = [
    url('^me/$', views.PostListUser.as_view()),
    path('profile/', views.ProfileTags.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
    path('all/', views.UserProfile.as_view({'get': 'list'})),



    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^.*$',IndexTemplateView.as_view(),name='entry point')





]
