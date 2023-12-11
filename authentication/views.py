from django.shortcuts import render
from . import views

def login(request):
    return render(request, 'login.html', {})

def schedule(request):
    return render(request, 'schedule.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def resources(request):
    return render(request, 'resources', {})