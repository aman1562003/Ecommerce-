from django import forms
from .models import Productdata, userdetails, Userimage, Businessdetails, BuyProduct
from django.forms import ModelForm
    
    

# class dataform(forms.Form):
class DataForm(ModelForm):
    class Meta:
        model = Productdata
        fields = ['product_name','product_descrition','product_prize','product_image']
        # ,'product_image'


class UserForm(ModelForm):
    class Meta:
        model = userdetails
        fields = ['name','about','phone','address1','address2','pincode','city','country']

class UserimageForm(ModelForm):
    class Meta:
        model = Userimage
        fields = ['user_image']

class businessForm(ModelForm):
    class Meta:
        model = Businessdetails
        fields = ['business_type', 'business_description', 'business_location']

class BuyProductForm(ModelForm):
    product_name = forms.CharField(max_length=200)
    seller_username = forms.CharField(max_length=200)
    product_id = forms.CharField(max_length=200)
    class Meta:
        model = BuyProduct
        fields = ['name','phone','address1','address2','pincode','city','country']
           