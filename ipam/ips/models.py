# https://docs.djangoproject.com/en/4.2/topics/db/models/
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#referencing-the-user-model
User = get_user_model() 

# class Post(models.Model):
#     text = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # name = models.CharField(max_length=200)
    # description = models.TextField()    
    # on_main = models.BooleanField(default=True) 
    # text = models.TextField() 
    # pub_date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='posts'
    # ) 

class SubnetModel(models.Model): 
    cidr = models.CharField(max_length=18)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class IPAddressModel(models.Model):
    STATUS_CHOICES = (
        ("FREE", "free"),
        ("USED", "used")   
    )
    subnet = models.ForeignKey(SubnetModel, on_delete=models.CASCADE)
    # ip_address = models.GenericIPAddressField(primary_key=True, unique=True)
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.CharField(choices = STATUS_CHOICES, max_length=4, default = 'free')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    mac_address = models.CharField(max_length=18)
    comment = models.TextField()
    last_seen = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class EventModel(models.Model): 
#     EVENT_TYPE_CHOICES = [
#         ("RESERVED", "reserved"),
#         ("RELEASED", "released"),
#         ("ARPING_RESPONSE", "arping_response")
#     ]
#     # ip_address_id
#     user_id = models.ForeignKey(User)
#     event_type = models.CharField(choices = EVENT_TYPE_CHOICES, max_length=15)
#     created_at = models.DateTimeField(auto_now_add=True)
