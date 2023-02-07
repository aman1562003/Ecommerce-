import uuid
from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class productdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_descrition = models.CharField(max_length=500)
    product_prize = models.IntegerField()
    product_image = models.ImageField(upload_to='media/files/photos', default="media/file/photos/OIP_1.jfif")

    def __str__(self):
        return self.product_name

