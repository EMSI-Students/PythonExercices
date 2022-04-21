from django.http import HttpResponse
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
    msg = "<h1>Products</h1>"
    msg += "<ul>"
    for product in products:
        msg += f"<li>{product.name} - {product.year} from {product.brand}</li>"
    msg += "</ul>"
    return HttpResponse(msg)

def products_year(request, year):
    msg = "<h1>Products</h1>"
    msg += "<ul>"
    for product in products:
        if product.year == year:
            msg += f"<li>{product.name} - {product.year} from {product.brand}</li>"
    msg += "</ul>"
    return HttpResponse(msg)

def products_name(request, name):
    full_name = " ".join(name.split('_'))
    msg = "<h1>Products</h1>"
    msg += "<ul>"
    for product in products:
        if product.name.lower() == full_name.lower():
            msg += f"<li>{product.name} - {product.year} from {product.brand}</li>"
    msg += "</ul>"
    return HttpResponse(msg)
