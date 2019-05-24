from django import forms
from django.contrib.auth import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
