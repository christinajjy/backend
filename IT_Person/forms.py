from django import forms
from .models import Pemails

class Pemails_form(forms.ModelForm):
    class Meta:
        model = Pemails
        fields =['pemail','apppwd']