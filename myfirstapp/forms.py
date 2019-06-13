from django import forms

class RegistrationForm(forms.Form):
    f_name=forms.CharField(max_length=20)
    l_name=forms.CharField(max_length=20)
    email= forms.EmailField()