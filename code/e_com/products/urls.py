from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.products_list, name = 'products_list'),
    path('<int:year>', views.products_year, name = 'products_year'),
    path('name/<slug:name>', views.products_name, name = 'products_name'),
    path('brand/<slug:brand>', views.products_brand, name = 'products_brand'),
]
