from django import forms
from .models import user
from django.forms import ModelForm
    
    

# class dataform(forms.Form):
class UserForm(ModelForm):
    class Meta:
        model = user
        fields = ['user_name','user_email','user_image']
        # ,'product_image'

        