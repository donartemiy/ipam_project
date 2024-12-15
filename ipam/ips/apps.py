# https://docs.djangoproject.com/en/4.2/ref/applications/#configuring-applications
from django.apps import AppConfig


class IpsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ips'
