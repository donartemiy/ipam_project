# https://docs.djangoproject.com/en/4.2/ref/django-admin/
from django.contrib import admin
from .models import IPAddressModel, SubnetModel

admin.site.register(IPAddressModel) 
admin.site.register(SubnetModel) 