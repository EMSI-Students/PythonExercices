from django.shortcuts import render
from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {'list_products': products})

def products_year(request, year):

    products = Product.objects.filter(date_production__year=year)
    return render(request, "products/products_list.html", {'list_products': products})

def products_name(request, name):
    full_name = " ".join(name.split('_'))
    products = Product.objects.filter(name=full_name)
    return render(request, "products/products_list.html", {'list_products': products})

def products_brand(request, brand):
    products = Product.objects.filter(brand=brand)
    return render(request, "products/products_list.html", {'list_products': products})

def product_info(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "products/product_info.html", {'product': product})
