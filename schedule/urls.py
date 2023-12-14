# scheduler_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("login/schedule/", views.schedule, name="schedule"),
]
