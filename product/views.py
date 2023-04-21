
from tkinter import Image
import uuid
from django.http import Http404
from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib import messages
from .forms import DataForm, UserForm,UserimageForm,businessForm, BuyProductForm
from .models import Productdata, userdetails,Userimage,Businessdetails, BuyProduct
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
    


@login_required
def businessdata(request):

    if request.method == 'POST':
        print(6)
        if 'form3_submit' in request.POST:
            form3 = businessForm(request.POST , request.FILES)
        
            if form3.is_valid():
                # print(form.cleaned_data)
                product = form3.save(commit=False)
                product.user = request.user
                product.save()
            # obj = form.instance
                print(5)
                return redirect(reverse('product:business'))
            # return render(request,'product/productdata.html')
            else:
            
                form3 = businessForm(instance=request.user)
                Business_detail = Businessdetails.objects.filter(user=request.user)
                messages.error(request, "Error Occured while submitting data")
                return render(request,'product/business.html', context={'form3':form3,'Business_detail': Business_detail,} )
               

    else:
        form3 = businessForm(instance=request.user)
        if request.user.is_authenticated:
            print(7)
            Business_detail = Businessdetails.objects.filter(user=request.user)
        else:
            contexts = None
        return render(request,'product/editprofile.html', context={'form3':form3,'Business_detail': Business_detail} )
    
        # form3 = businessForm()
        # print(2)
        # return render(request,'product/editprofile.html', context={'form3':form3})


 
# def productview(request):
#     print(3)
#     product_list = Productdata.objects.all()
#     context = {
#         'product_list': product_list,
#     }
#     return render(request,'product/Product.html', context)



def productview(request):
    if request.method == 'POST':
        
        print(0)
        if 'form_submit' in request.POST:
            form = BuyProductForm(request.POST, request.FILES)
            if form.is_valid():  
                userdetail = userdetails.objects.get(user=request.user)
                buydetail = form.save(commit=False)
                buydetail.user = request.user
                buydetail.product_name = form.cleaned_data['product_name']
                buydetail.seller_username = form.cleaned_data['seller_username']
                buydetail.product_id = form.cleaned_data['product_id']
                buydetail.name = userdetail.name
                buydetail.phone =  userdetail.phone
                buydetail.address1 =  userdetail.address1
                buydetail.address2 =  userdetail.address2
                buydetail.pincode  =  userdetail.pincode
                buydetail.city     =  userdetail.city
                buydetail.country  =  userdetail.country 
                print(form.cleaned_data)
                print(request.FILES)
                
                buydetail.save()
                print(1)
                return redirect(reverse('product:product'))
        else:
            print(3)
            form = BuyProductForm(instance=request.user)
            
            product_list = Productdata.objects.all()
            
            messages.error(request, "Error Occured while submitting data")
            return render(request,'product/Product.html', context={'form':form,'product_list': product_list} )
               

    else:
        form = BuyProductForm(request.POST,instance=request.user)
      
        print(2)
        product_list = Productdata.objects.all()
        
        contexts = None
        return render(request,'product/Product.html', context={'form':form,'product_list': product_list} )
    



    
    

   
        

        
    
    


    
    


