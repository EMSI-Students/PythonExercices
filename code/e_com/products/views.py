from django.shortcuts import render
from .models import Product

products = Product.objects.all()

def products_list(request):
    return render(request, "products/products_list.html", {'list_products': products})


def products_year(request, year):
    return render(request, "products/products_list_year.html", {'list_products': products, 'year': year})

def products_name(request, name):
    full_name = " ".join(name.split('_'))
    return render(request, "products/products_list_name.html", {'list_products': products, 'name': full_name})

def products_brand(request, brand):
    return render(request, "products/products_list_brand.html", {'list_products': products, 'brand': brand})
