from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('charge/', views.ChargeView.as_view()),
]
