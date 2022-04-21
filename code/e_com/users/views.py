from django.http import HttpResponse

def register(request):
    return HttpResponse("<h1>Welcome to Registration Page</h1>")

def login(request):
    return HttpResponse("<h1>Welcome to Login Page</h1>")

def change_password(request):
    return HttpResponse("<h1>Welcome to Change Password Page</h1>")

def hello(request, user_name='', user_age=0):
    if user_name == '':
        msg = "<h1>Hello, Welcome to this Website</h1>"
    elif user_age == 0:
        msg = f"<h1>Hello {user_name}, Welcome to this Website</h1>"
    else :
        msg = f"<h1>Hello {user_name}, You are {user_age} Years Old, Welcome to this Website</h1>"

    return HttpResponse(msg)
