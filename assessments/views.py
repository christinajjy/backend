from django.shortcuts import render
from .models import Quiz
from .forms import QuestionForm

def assessment(request):
    assessment_questions = Quiz.objects.all()
    
    return render(request,'assessment.html',{
        'assessment_questions': assessment_questions,
    })
