from django.db import models
from django import forms

# Create your models here.
class Answers(models.Model):
    question_id=models.CharField(max_length=10)
    answer =models.CharField(max_length=2)
    def __str__(self):
        return self.question_id

class quiz1(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200)
    option_B=models.CharField(max_length=200)
    option_C=models.CharField(max_length=200)
    option_D=models.CharField(max_length=200)
    answer_option=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    
