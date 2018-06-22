from django.contrib import admin
from .models import Category
from .models import Pricelist
# Register your models here.
admin.site.register(Category)
admin.site.register(Pricelist)
