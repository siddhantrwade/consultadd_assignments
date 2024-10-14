'''
This module/file will hold various forms for registration and profile updates to provide users with a GUI
'''

from django import forms 
from .models import UserDetails

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']




    


