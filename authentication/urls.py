from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('home/',views.home,name="home"),
    path('login/signup/', views.signup, name="signup"),    
]