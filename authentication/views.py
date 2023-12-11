from django.shortcuts import render
from . import views

# Create your views here.

def login(request):
    return render(request, 'login.html', {})