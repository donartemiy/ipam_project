# https://docs.djangoproject.com/en/4.2/ref/django-admin/
from django.contrib import admin
from .models import IPAddressModel, SubnetModel

# admin.site.register(IPAddressModel) 
# admin.site.register(SubnetModel) 

@admin.register(IPAddressModel)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'status', 
                    'user', 'mac_address', 
                    'comment', 'last_seen', 
                    'created_at', 'updated_at')
    search_fields = ('ip_address',)
    list_filter = ('last_seen',)

@admin.register(SubnetModel)
class SubnetAdmin(admin.ModelAdmin):
    list_display = ('cidr', 'description', 
                    'created_at')
