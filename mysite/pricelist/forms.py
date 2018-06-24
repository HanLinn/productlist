from django import forms
from .models import Pricelist
from django.forms import ModelForm


class detail(ModelForm):
    class Meta:
        model = Pricelist
        fields = ['name', 'price', 'category']
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Name','class': "mm",'class':"form-control"}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price','class': "mm",'class':"form-control"}),
            'category': forms.Select(attrs={'placeholder': 'category',"class": "mm",'class':"form-control"})
        }

        
