# https://docs.djangoproject.com/en/4.2/topics/http/urls/

from django.urls import path
from . import views

app_name = 'ips'

urlpatterns = [
    path('ips/<str:ip>/', views.ips_detail, name='var_ips_detail'),
    path('ips/', views.ips_list, name='var_ips'),
    # path('', views.index),
    path('', views.IndexView.as_view(), name='var_index'),
] 