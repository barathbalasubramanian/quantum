from django.shortcuts import render , redirect
from django.http import HttpResponse
from firstapp.models import Product , UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return render(request , "index.html")

def add_products_view(request):
    user = request.user
    print(user)
    if request.method == "POST":
        index = 0
        while f"product_name_{index}" in request.POST:
            name = request.POST[f"product_name_{index}"]
            price = request.POST[f"product_price_{index}"]
            Product.objects.create(username=user , name=name, price=price)
            index += 1
        return render(request, 'added.html')
    return render(request, "add_product.html")





@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        domain = request.POST.get('domain')

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()

        profile = UserProfile(user=my_user, phone=phone, address=address, domain=domain)
        profile.save()
        
        return redirect('login')

    return render(request ,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
                login(request,user)
                print('Loginned' )
                return redirect('home')
            
    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
