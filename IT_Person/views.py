from django.shortcuts import render,redirect
from .forms import Pemails_form
from .models import Pemails

def phish(request):
    phishing_emails=Pemails.objects.all()
    return render(request,"IT_person/phishingmail.html",{
        'phishing_emails':phishing_emails
    })
def analytics(request):
    return render(request,"IT_person/analytics.html",{})

def pemailinput(request):
    if request.method == 'POST':
        form = Pemails_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pemailinput')
    else:
        pass
    
    return render(request,'IT_person/loginpage.html',{'form':Pemails_form})

