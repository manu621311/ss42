"""ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
# from core.views import IndexTemplateView
# from  rest_framework.authtoken.views import obtain_auth_token
# from django_registration.backends.one_step.views import RegistrationView
# from django_registration.backends.one_step import RegistrationView
# from django_registration.backends.one_step.views import RegistrationView

# from django_registration.one_step.views import RegistrationView
# from users.forms import CustomUserForm
# from accounts import views
from .views import SocialLoginView
urlpatterns = [

    # path('sign_up/', views.SignUp.as_view(), name="sign_up"),
    path('', SocialLoginView.as_view()),
    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^.*$',IndexTemplateView.as_view(),name='entry point')





]
