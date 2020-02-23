from django.shortcuts import render, redirect
from .models import Category
from .models import Pricelist
from .forms import detail


def index(request):
    productlist=Pricelist.objects.all()
    categorylist = Category.objects.all()
    context = {'productlist': productlist,'categorylist' : categorylist}
    return render(request, 'pricelist/pricelist.html', context)


def productlist(request):
    #productlist = Pricelist.objects.filter(category_id=category_name_id)
    categorylist = Category.objects.all()
    productlist=Pricelist.objects.all()
    context = {'productlist': productlist,'categorylist' : categorylist}
    return render(request, 'pricelist/pricelist.html', context)


def product_update(request, id):
    product = Pricelist.objects.get(id=id)
    form = detail(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'pricelist/detail.html', {'form':form,'product':product})

def product_create(request):
    form=detail(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'pricelist/detail.html',{'form':form})

def product_delete(request,id):
    product=Pricelist.objects.get(id=id)

    if request.method=="POST":
        product.delete()
        return redirect('index')
    return render(request,'pricelist/product_delete_comfirm.html',{'product':product})
