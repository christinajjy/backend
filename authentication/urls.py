from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    path('assessments/', include('assessments.urls', namespace='assessments')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('resources/', include('resources.urls', namespace='resources')),
]