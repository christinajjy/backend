from django.shortcuts import render,redirect
from .forms import Pemails_form

def phish(request):
    return render(request,"IT_person/phishingmail.html",{})
def analytics(request):
    return render(request,"IT_person/analytics.html",{})

def pemailinput(request):
    if request.method == 'POST':
        form = Pemails_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        pass
    
    return render(request,'IT_person/loginpage.html',{'form':Pemails_form})

