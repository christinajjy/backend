from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('phish/',views.phish,name="phish"),
    path('phish/',views.dropdown,name="phish"),
    path('analytics/', views.analytics, name="analytics"),
]