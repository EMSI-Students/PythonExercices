from django.shortcuts import render
from .product import Product

products = []
products.append(Product('Macbook Air', 'Apple', 2021))
products.append(Product('Macbook Air', 'Apple', 2020))
products.append(Product('Macbook Pro', 'Apple', 2021))
products.append(Product('Macbook Pro', 'Apple', 2020))
products.append(Product('Thinkpad X', 'Lenovo', 2018))
products.append(Product('EliteBook', 'Hp', 2018))
products.append(Product('Airpods Pro', 'Apple', 2020))


def products_list(request):
    return render(request, "products/products_list.html", {'list_products': products})


def products_year(request, year):
    return render(request, "products/products_list_year.html", {'list_products': products, 'year': year})


def products_name(request, name):
    full_name = " ".join(name.split('_'))
    return render(request, "products/products_list_name.html", {'list_products': products, 'name': full_name})
