
from tkinter import Image
import uuid
from django.http import Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import DataForm
from .models import Productdata
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def productdata(request):

    if request.method == 'POST':
        form = DataForm(request.POST , request.FILES)
        
        if form.is_valid():
            # print(form.cleaned_data)
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            # obj = form.instance
            print(0)
            return redirect(reverse('product:productdata'))
            # return render(request,'product/productdata.html')

    else:
        form = DataForm()
        print(2)
        return render(request,'product/productdata.html', context={'form':form})

def thanku(request):
    print(1)
    return render(request,'product/thanku.html')    

def profile2(request):
    product_list = Productdata.objects.filter(user=request.user)
    context = {
        'product_list': product_list,
    }
    return render(request, 'product/profile2.html', context)


