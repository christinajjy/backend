from django.shortcuts import render
from .models import quiz1
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('agg')


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
        percent = 100 - (score/(total*10) *100)


        labels = ['Correct', 'Wrong']
        sizes = [correct, wrong]
        explode = (0.1, 0)  # explode 1st slice

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Save the chart to a BytesIO buffer
        chart_buffer = BytesIO()
        plt.savefig(chart_buffer, format='png')
        chart_buffer.seek(0)
        chart_data = base64.b64encode(chart_buffer.getvalue()).decode('utf-8')
        plt.close()



        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'chart_data': chart_data,
        }
        return render(request,'assessments/results.html',context)
    else:
        question=quiz1.objects.all()
        context = {
            'question':question
        }
        return render(request,'assessments/assessments.html',context)

