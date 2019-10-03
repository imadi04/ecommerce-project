from django.shortcuts import render
from django.views.generic import View
from cart.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from cart.models import Product,Order,OrderUpdate
from math import ceil
import json
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,"cart/index.html")

@login_required(login_url='/cart/user_login')
def products(request):
    product=Product.objects.all()
    n=len(product)
    nrows= n//4 + ceil((n/4)-(n//4))
    params={'no_of_rows':nrows,'range':range(0,n),'product':product}
    return render(request,"cart/products.html",params)

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'cart/tracker.html')

@login_required(login_url='/cart/user_login')
def cart(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Order(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        id = order.order_id
        return render(request,"cart/index.html")
    return render(request,"cart/cart.html")


@login_required
def user_logout(request):
    logout(request)
    return render(request,"cart/index.html")#HttpResponseRedirect(reverse('cart/index.html'))


def register(request):

    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'cart/registration.html',
                                  {'user_form':user_form,
                                  'profile_form':profile_form,
                                  'registered':registered})




def user_login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'cart/index.html')
            else:
                return HttpResponse('Account not Active')
        else:
            print("Someone tried to login but failed !")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Invalid login details passed !")
    else:
        return render(request,'cart/login.html',{})
