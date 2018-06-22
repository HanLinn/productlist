from django import forms
from .models import Pricelist
from django.forms import ModelForm


class detail(ModelForm):
    class Meta:
        model = Pricelist
        fields = ['name', 'price', 'category']
