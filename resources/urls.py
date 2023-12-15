from django.contrib import admin
from django.urls import path, include
from . import views

app_name='resources'

urlpatterns = [
    path('resources/', views.resources, name="resources"),
]