from django.shortcuts import render, redirect
from .models import Category
from .models import Pricelist
from .forms import detail


def index(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'pricelist/category.html', context)


def productlist(request, category_name_id):
    productlist = Pricelist.objects.filter(category_id=category_name_id)
    context = {'productlist': productlist}
    return render(request, 'pricelist/pricelist.html', context)


def product_update(request, id):
    product = Pricelist.objects.get(id=id)
    form = detail(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'pricelist/detail.html', {'form':form,'product':product})
