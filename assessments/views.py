from django.shortcuts import render
from .models import Quiz
#from .forms import QuestionForm

def assessments(request):
    assessment_questions = Quiz.objects.all()
    
    return render(request,'assessments.html',{
        'assessment_questions': assessment_questions,
    })
