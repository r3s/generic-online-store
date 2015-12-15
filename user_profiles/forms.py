from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password =  forms.CharField(widget=forms.PasswordInput, min_length=3)

class RegForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password =  forms.CharField(widget=forms.PasswordInput, min_length=3)
    password_again =  forms.CharField(widget=forms.PasswordInput, min_length=3)
    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError("Passwords does not match !")
        return password_again
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account already exist for this email address.")
        return email
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username
