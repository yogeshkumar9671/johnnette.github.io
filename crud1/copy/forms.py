from django import forms
from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

from new_app.models import AddressModel

class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = "__all__"

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
    

class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Password"}))