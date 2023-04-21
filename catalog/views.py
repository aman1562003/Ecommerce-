from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from .models import 
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from product.views import productdata, profile2, userdata, productview, businessdata
from product.models import Productdata
# Create your views here.

@login_required
def profile(request):
    return render(request,'catalog/profile.html')


class SignUpView(CreateView):
   form_class = UserCreationForm
   success_url  = reverse_lazy('login')
   template_name = 'catalog/signup.html'


def home(request):
    print(1)
    product_list = Productdata.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request,'catalog/home.html', context)   





# def login(request):
#     return render(request,'templates/login.html')

# def profilepic(request):
#     if request.method == 'POST':
#         user_profile = user.objects.get(user=request.user)
#         user_profile.profile_picture = request.FILES['profile_picture']
#         user_profile.save()
#         return redirect('profile')
#     return render(request, 'profile.html')
