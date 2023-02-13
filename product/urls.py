from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('productdata/', views.productdata, name='productdata'),
    path('editprofile/',views.userdata,name = 'editprofile'),
    path('thanku/', views.thanku,name='thanku'),
]
