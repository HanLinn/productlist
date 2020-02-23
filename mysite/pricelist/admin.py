from django.contrib import admin
from .models import Category,unit
from .models import Pricelist
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(unit)

@admin.register(Pricelist)
class CustomerInformation(ImportExportModelAdmin):
    list_display = ('name','price','category','tags')
    search_fields = ['name','price','category','tags']
    pass

@admin.register(Category)
class Category(ImportExportModelAdmin):
    list_display = ('category_name',)
    search_fields = ['category_name',]
    pass
