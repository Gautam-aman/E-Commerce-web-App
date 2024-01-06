from django.shortcuts import render, redirect
from .models import Person
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail 

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
@login_required
def contact(request):
    return render (request, "home/templates/contact.html")
        
        
def about(request):
    return render(request, "home/templates/about.html")

def test (request):
    return render(request, "home/templates/home1.html")



@login_required
def cart(request):
    return render(request, "home/templates/cart.html")


def Ccontact(request):
    if request.method=="POST":
        data= request.POST
        fname= data.get('Cname')
        fmail=data.get('Cemail')
        desc= data.get('Cmessage')
        
        query= contact(name=fname, email=fmail,
                     description=desc)
        query.save()
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get.connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {fname}' , f'UserEmail: {fmail}, query:{desc}', from_email,['rigel2128@gmail.com'],
                                        connection=connection)
        connection.send_message([email_message])
        connection.close()
        return redirect("/contact/")
    return render(request, "home/templates/contact.html")
        
        
        
        
      


