# forms.py
from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ['email', 'password']