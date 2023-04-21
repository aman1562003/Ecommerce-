from django.contrib import admin
from .models import Productdata,userdetails,Userimage, Businessdetails, BuyProduct
# Register your models here.

admin.site.register(Productdata)
admin.site.register(userdetails)
admin.site.register(Userimage)
admin.site.register(Businessdetails)
admin.site.register(BuyProduct)
