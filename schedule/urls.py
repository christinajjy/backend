# scheduler_app/urls.py

from django.urls import path
from . import views

app_name='schedule'
urlpatterns = [
    path("schedule/", views.schedule, name="schedule"),
]
