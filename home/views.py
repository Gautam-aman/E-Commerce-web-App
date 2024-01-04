from django.shortcuts import render, redirect
from .models import Person
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.



def home (request):
    return render(request, "home/templates/home.html")

def login1 (request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password= data.get('password')
        
        user = User.objects.all()
        if not User.objects.filter(username=username):
            messages.warning(request," User does not exist")
        user= authenticate(username=username,password=password)
        if user is None:
            messages.warning(request, "Invalid credentials")
            return redirect ("/login/")
        else:
            login(request,user)
            return redirect("/home/")
        
    return render(request, "home/templates/login.html")

def register(request):
    if request.method=="POST":
        data= request.POST
        username= data.get('username')
        password=data.get('password')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User already Exist")
            return redirect('/register/')
        else:
            user= User.objects.create(username=username)
            user.set_password(password)
            user.save()
            messages.info(request, "Your Account is created")
            return redirect("/login/")
        
    return render(request,'register.html')
        
