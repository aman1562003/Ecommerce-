from django import forms
from .models import productdata
from django.forms import ModelForm
    
    

# class dataform(forms.Form):
class DataForm(ModelForm):
    class Meta:
        model = productdata
        fields = ['product_name','product_descrition','product_prize','product_image']
        # ,'product_image'