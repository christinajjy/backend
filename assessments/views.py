from django.shortcuts import render
from .models import quiz1
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse


def assessments(request):
    assessment_questions = quiz1.objects.all()
    
    return render(request,'assessments/assessments.html',{
        'assessment_questions': assessment_questions,
    })


def result(request):
    if request.method == 'POST':
        print(request.POST)
        question=quiz1.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in question:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer_option)
            print()
            if q.answer_option ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'assessments/results.html',context)
    else:
        question=quiz1.objects.all()
        context = {
            'question':question
        }
        return render(request,'assessments/assessments.html',context)
