# https://docs.djangoproject.com/en/4.2/topics/db/models/
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#referencing-the-user-model
User = get_user_model() 

class SubnetModel(models.Model): 
    cidr = models.CharField(max_length=18)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cidr


class IPAddressModel(models.Model):
    STATUS_CHOICES = (
        ("free", "free"),
        ("used", "used")   
    )
    subnet = models.ForeignKey(SubnetModel, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.CharField(choices = STATUS_CHOICES, max_length=4)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='ip_user')
    mac_address = models.CharField(null=True, max_length=18)
    comment = models.TextField(null=True, blank=True, max_length=61)
    last_seen = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    
    def __str__(self):
        return self.ip_address
