# https://docs.djangoproject.com/en/4.2/topics/http/urls/

from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('', views.index),
    path('ips/', views.ips_list),
    path('ips/<str:pk>/', views.ips_detail),
] 