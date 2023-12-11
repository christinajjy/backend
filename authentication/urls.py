from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('schedule/', views.schedule, name="schedule"),
    path('signup/', views.signup, name="signup"),
    path('resources/', views.resources, name="resources"),
]