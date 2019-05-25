from django import forms
from django.contrib.auth.models import User

OFFICE_CHOICES = (('Gerente', 'Gerente'), ('Funcionário', 'Funcionário'))


class UserAddForm(forms.Form):

    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    office = forms.ChoiceField(label='Cargo', choices=OFFICE_CHOICES)
