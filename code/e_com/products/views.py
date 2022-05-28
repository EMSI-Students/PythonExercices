from django.shortcuts import render
from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {'list_products': products})

def products_year(request, year):
    products = Product.objects.filter(year=year)
    return render(request, "products/products_list.html", {'list_products': products})

def products_name(request, name):
    full_name = " ".join(name.split('_'))
    products = Product.objects.filter(name=full_name)
    return render(request, "products/products_list.html", {'list_products': products})

def products_brand(request, brand):
    products = Product.objects.filter(brand=brand)
    return render(request, "products/products_list.html", {'list_products': products})
