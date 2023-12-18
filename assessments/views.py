from django.shortcuts import render
from .models import Quiz
from .models import Answers

def assessment(request):
    assessment_questions = Quiz.objects.all()
    assessment_answers = Answers.objects.all()
    
    return render(request,'assessments.html',{
        'assessment_questions': assessment_questions,
        'assessment_answers': assessment_answers,
    })
