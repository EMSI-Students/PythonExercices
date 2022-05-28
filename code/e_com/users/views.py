from django.shortcuts import render
from .models import User

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def change_password(request):
    return render(request, "users/change_password.html")

def hello(request, user_name='', user_age=0):
    return render(request, "users/hello.html", {'user_name': user_name, 'user_age': user_age})

def user_info(request, user_id):
    user = User.objects.get(pk=user_id)
    products = user.product_set.all()
    context = {'user': user, 'products': products}

    return render(request, "users/user_info.html", context=context)
