from django import forms
from .models import Productdata, userdetails, Userimage
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