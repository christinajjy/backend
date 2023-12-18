from django.urls import path
from . import views

urlpatterns = [
    path('assessments', views.assessment,name="assessment_questions"),
    path('assessments', views.assessment,name="assessment_answers"),
    
]