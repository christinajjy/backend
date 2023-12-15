from django.shortcuts import render

def schedule(request):
    return render(request, 'cal.html', {})
