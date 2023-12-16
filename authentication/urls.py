from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    path('assessments/', include('assessments.urls', namespace='nav_assessments')),
    path('schedule/', include('schedule.urls', namespace='nav_schedule')),
    path('resources/', include('resources.urls', namespace='nav_resources')),
]