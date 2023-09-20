from django import forms
from .models import my_cv
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class register_from(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'})
            
        }



class cv_form(forms.ModelForm):

    class Meta:

        model = my_cv
        fields = ('__all__')

