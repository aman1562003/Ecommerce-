from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('productdata/', views.productdata, name='productdata'),
    path('thanku/', views.thanku,name='thanku'),
]
