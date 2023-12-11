from django.shortcuts import render
from . import views

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})
