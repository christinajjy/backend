from django.db import models
from django import forms

# Create your models here.
class Answers(models.Model):
    question_id=models.CharField(max_length=10)
    answer =models.CharField(max_length=2)
    def __str__(self):
        return self.question_id

class Quiz(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    question_difficulty=models.CharField(max_length=200)
    option_A=models.CharField(max_length=200)
    option_B=models.CharField(max_length=200)
    option_C=models.CharField(max_length=200)
    option_D=models.CharField(max_length=200)
    answers =models.ForeignKey(Answers,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.question_id
    
