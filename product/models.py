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
    product_descrition = models.CharField(max_length=500)
    product_prize = models.IntegerField()
    product_image = models.ImageField(upload_to=upload_to, default="media/file/photos/OIP_1.png")
    # product_image = models.ImageField(upload_to='media/files/photos', default="media/file/photos/OIP_1.png")

    def __str__(self):
        return f"{self.product_name}"

