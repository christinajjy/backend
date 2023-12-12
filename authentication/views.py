from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import views

# Create your views here.
def home(request):
    return render(request,"home.html",{})
def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,("there was an error logging in"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})

def login_return(request):
    return redirect ('login')
