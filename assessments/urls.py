from django.urls import path
from . import views

app_name='assessments'
urlpatterns = [
    path('assessments', views.assessments, name="assessments"),
    path('addQuestion/', views.addQuestion,name="addQuestion"),
    path('assessments/', views.result,name="result"),
]