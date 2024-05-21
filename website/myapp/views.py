from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, "index.html")

def shop(request):

    return render(request, "shop.html")

def shopdetail (request):

    return render(request,'shop-detail.html')

@login_required(login_url="login.html")
def cart(request):

    return render(request,'cart.html')

def chackout(request):

    return render(request,"chackout.html")

def testimonial(request):

    return render(request,'testimonial.html')

def four(request):
    return render(request,'404.html')

def contact(request):
    return render(request,'contact.html')

def error(request):
    return render(request,'404.html')

def login1(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get("uname")
        password = data.get("password")
        User.objects.get(username)
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid credentials")
            return redirect("login.html")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login.html")
        else:
            login(request,user)
            logged_in_user = request.user
            # Pass user data to the template
            return render(request, 'cart.html', {'logged_in_user': logged_in_user})
        
    
        
    return render(request,'login.html')

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("fname")
        lname = data.get("lname")
        uname = data.get("uname")
        password = data.get("password")
        email =data.get("email")
        
        if User.objects.filter(username=uname).exists():
            messages.info(request,"Username exists !!!")
            return redirect("reg")

        else:
            user =  User.objects.create(first_name=fname,email=email,last_name=lname,username=uname)
            user.set_password(password)
            user.save()
            messages.info(request,"Registration successfully !!!")
            return redirect("reg")

    return render(request, 'registration.html')

def logoutpage(request):
    logout(request)
    return render(request,"login.html")