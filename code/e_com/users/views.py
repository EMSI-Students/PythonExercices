from django.shortcuts import render

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def change_password(request):
    return render(request, "users/change_password.html")

def hello(request, user_name='', user_age=0):
    return render(request, "users/hello.html", {'user_name': user_name, 'user_age': user_age})
