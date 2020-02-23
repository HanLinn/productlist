from django import forms
from .models import Pricelist
from django.forms import ModelForm


class detail(ModelForm):
    class Meta:
        model = Pricelist
        fields = ['name', 'price', 'category','base_currency','tags','Unit']
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Name','class': "mm",'class':"form-control"}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price','class': "mm",'class':"form-control"}),
            'category': forms.Select(attrs={'placeholder': 'category',"class": "mm",'class':"form-control"}),
            'base_currency': forms.Select(attrs={'placeholder': 'currency',"class": "mm",'class':"form-control"}),
            'tags': forms.TextInput(attrs={'placeholder': 'tags','class': "mm",'class':"form-control"}),
            'Unit': forms.Select(attrs={'placeholder': 'Unit',"class": "mm",'class':"form-control"}),
        }

        
