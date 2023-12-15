from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication/signup.html')
        else:
            messages.success(request,("there was an error logging in"))
            return redirect('authentication/login.html')
    else:
        return render(request, 'authentication/login.html', {})

def signup(response):
    if response.method=="POST":
        form =RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form=RegisterForm()

    return render(response,"authentication/signup.html",{"form":form})

