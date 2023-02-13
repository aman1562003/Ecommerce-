# urls for my catalog
from django.urls import path,include
# from mysite import mysite
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    # path('home',views.home,name = 'home'),
    path('signup/', views.SignUpView.as_view(), name= 'signup'),
    path('login/', views.home, name ='home' ),
    path('product/',include('product.urls')),
    path('product/productdata/', views.productdata, name='productdata'),
    path('product/profile2/',views.profile2,name = 'profile2' ),
    path('product/editprofile/',views.userdata,name = 'editprofile' ),
    path('profile/',views.profile,name='profile'),
    
   
]