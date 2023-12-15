from django import forms

class Phishingemails(forms.Form):
    email = forms.CharField(max_length = 200)
    app_passwords = forms.CharField(widget = forms.PasswordInput())