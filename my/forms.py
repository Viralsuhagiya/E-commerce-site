from django import forms
from .models import  Registration,Hobby
from django.forms.widgets import CheckboxSelectMultiple


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control',
                                                                            'placeholder':'Username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                            'placeholder':'Password'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control',
                                                                            'placeholder':'Email '}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control',
                                                                   'placeholder':'Phone '}))



class RegistrationModelForm(forms.ModelForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Password'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Email '}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Phone '}))
    image = forms.ImageField()
    class Meta:
        model = Registration
        fields = [
            'username',
            'password',
            'email',
            'phone',
            'gender',
            'country',
            'hobby',
            'image',
        ]
        def __init__(self, *args, **kwargs):
            super(RegistrationModelForm, self).__init__(*args, **kwargs)

            self.fields["hobby"].widget = CheckboxSelectMultiple()
            self.fields["hobby"].queryset = Hobby.objects.all()
