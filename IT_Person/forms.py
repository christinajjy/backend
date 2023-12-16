from django import forms
from .models import Pemails
from .models import Pemails_content

class Pemails_form(forms.ModelForm):
    class Meta:
        model = Pemails
        fields =['pemail','apppwd']

class Pemails_content(forms.ModelForm):
    class Meta:
        model = Pemails_content
        fields = ['pemail','emp_name','emp_email','recent_project']
