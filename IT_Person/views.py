from django.shortcuts import render
# from .models import Employees
# Create your views here.
def login(request):
    return render(request,"IT_person/loginpage.html",{})
def phish(request):
    return render(request,"IT_person/phishingmail.html",{})
def analytics(request):
    return render(request,"IT_person/analytics.html",{})
# def employee_list(request):
#     # data=Employees.objects.all();
#     return render(request,'phishingmail.html',{'data_from_db':data})
# def dropdown(request):
#     # data_f = Employees.objects.values_list("emailID", flat=True).distinct()
#     return render(request, 'phishingmail.html', {'data_f': data_f})

