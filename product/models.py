import os
import uuid
from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
def upload_to(instance, filename):
    return f'media/files/photos/{instance.user.username}/{instance.product_id}/{filename}'



class Productdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_descrition = models.TextField(max_length=500)
    product_prize = models.IntegerField()
    product_image = models.ImageField(upload_to=upload_to, default="media/file/photos/OIP_1.png")
    # product_image = models.ImageField(upload_to='media/files/photos', default="media/file/photos/OIP_1.png")

    def __str__(self):
        return f"{self.product_name}"




def upload_to_user(instance, filename):
    return f'media/files/photos/{instance.user.username}/{filename}'

class Userimage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to= upload_to_user, default="https://cdn-icons-png.flaticon.com/512/20/20079.png")
    def __str__(self):
        return f"{self.user.username}"

class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null = True,blank=True )    
    about = models.TextField(max_length=500,null = True,blank=True )
    phone = models.CharField(max_length=20,null = True,blank=True )
    address1 = models.CharField(max_length=200,null=True,blank=True )
    address2 = models.CharField(max_length=200,null = True,blank=True )
    pincode = models.CharField(max_length=20,null = True,blank=True )
    city = models.CharField(max_length=100,null = True,blank=True )
    country = models.CharField(max_length=20,null = True,blank=True )

    def __str__(self):
        return f"{self.user.username}"



