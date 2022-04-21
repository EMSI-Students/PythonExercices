from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name = 'products_list'),
    path('<int:year>', views.products_year, name = 'products_year'),
    path('<slug:name>', views.products_name, name = 'products_name'),
]
