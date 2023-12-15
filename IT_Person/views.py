from django.shortcuts import render
from .forms import InputForm
def pemailinput(request):
    return render(request,"IT_person/loginpage.html",{})
def phish(request):
    return render(request,"IT_person/phishingmail.html",{})
def analytics(request):
    return render(request,"IT_person/analytics.html",{})
def submit_pemai(request):
    context = {}
    context["form"] = InputForm()
    return render(request, "IT_person/loginpage.html",context)

