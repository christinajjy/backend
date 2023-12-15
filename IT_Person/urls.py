from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('IT/login/', views.login, name="login"),
    path('IT/phish/',views.phish,name="phish"),
    # path('phish/',views.dropdown,name="phish"),
    path('IT/analytics/', views.analytics, name="analytics"),
]