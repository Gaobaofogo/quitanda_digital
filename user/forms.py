from django import forms
from django.contrib.auth.models import User

OFFICE_CHOICES = (('Gerente', 'Gerente'), ('Funcionário', 'Funcionário'))


class UserAddForm(forms.Form):

    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    office = forms.ChoiceField(label='Cargo', choices=OFFICE_CHOICES)


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Digite seu usuário aqui...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Senha'}))
