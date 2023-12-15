from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    # path('base/',views.base,name="base")
    
]