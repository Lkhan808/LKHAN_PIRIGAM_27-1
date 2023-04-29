from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    password1 = forms.CharField(max_length=100, min_length=3, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, min_length=3, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=100, min_length=3, widget=forms.PasswordInput())
