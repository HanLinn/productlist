from django.db import models
from django.contrib.auth.models import User
from math import ceil

# Create your models here.
CURRENCY =[
    ('K','KYAT'),
    ('B','BAHT')
]

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class unit(models.Model):
    unit_name = models.CharField(max_length=5)

    def __str__(self):
        return self.unit_name 

        
class Pricelist(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete='CASCADE')
    base_currency = models.CharField(max_length=2,choices=CURRENCY)
    tags = models.CharField(max_length=150,null=True,blank=True)
    barcode = models.CharField(max_length=20,null=True,blank=True)
    Unit = models.ForeignKey(unit,on_delete='CASCADE',null=True,blank=True)
    cost = models.FloatField()
    

    def __str__(self):
        return self.name

    @property
    def priceinkyat(self):
        if self.base_currency == 'K':
            pricekyat = self.price
        else:
            pricekyat = ceil(self.price /0.021 / 100) * 100
        return pricekyat

    @property
    def priceinbaht(self):
        if self.base_currency == 'B':
            pricebaht = self.price
        else:
            pricebaht = int(self.price * 0.021)
        return pricebaht

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=25)

