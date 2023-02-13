
from tkinter import Image
import uuid
from django.http import Http404
from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib import messages
from .forms import DataForm, UserForm,UserimageForm
from .models import Productdata, userdetails,Userimage
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


@login_required
def profile2(request):
    if request.user.is_authenticated:
        product_list = Productdata.objects.filter(user=request.user)
        user_detail = Userimage.objects.filter(user=request.user)
        context = {
            'product_list': product_list,
            'user_detail': user_detail,
        }
    else:
        context = None    
    return render(request, 'product/profile2.html', context)


@login_required

def userdata(request):
    if request.method == 'POST':
        
        print(0)
        if 'form1_submit' in request.POST:
            form1 = UserimageForm(request.POST, request.FILES)
            if form1.is_valid():
                userimage = form1.save(commit=False)
                userimage.user = request.user
                userimage.user_image = form1.cleaned_data['user_image']  # Update the user_image field
                print(form1.cleaned_data)
                print(request.FILES)
                
                try:
                    old_image = Userimage.objects.get(user=request.user)
                    old_image.delete()
                except Userimage.DoesNotExist:
                    pass
                userimage.save()
                print(3)
                return redirect(reverse('product:editprofile'))
        elif 'form_submit' in request.POST:
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():  
                userdetail = form.save(commit=False)
                userdetail.user = request.user
                # userdetail = form.cleaned_data['name','about','phone','address1','address2','pincode','city','country']  # Update the user_image field
                print(form.cleaned_data)
                print(request.FILES)
                try:
                        old = userdetails.objects.get(user=request.user)
                    # if old.name != None:
                        old.delete()          
                except userdetails.DoesNotExist:
                        pass
                userdetail.save()
                print(1)
                return redirect(reverse('product:editprofile'))
        else:
            
            form = UserForm(instance=request.user)
            form1 = UserimageForm(instance=request.user)
            user_detail = userdetails.objects.filter(user=request.user)
            user_detail1 = Userimage.objects.filter(user=request.user)
            messages.error(request, "Error Occured while submitting data")
            return render(request,'product/editprofile.html', context={'form':form,'form1':form1,'user_detail': user_detail,'user_detail': user_detail1} )
               

    else:
        form = UserForm(instance=request.user)
        form1 = UserimageForm(instance=request.user)
        if request.user.is_authenticated:
            print(2)
            user_detail = userdetails.objects.filter(user=request.user)
            user_detail1 = Userimage.objects.filter(user=request.user)
        else:
            contexts = None
        return render(request,'product/editprofile.html', context={'form':form,'form1':form1,'user_detail': user_detail,'user_detail': user_detail1} )
    

   
        

        
    
    


    
    


