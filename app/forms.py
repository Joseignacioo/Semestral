from dataclasses import fields
from msilib.schema import Class
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    pass
    