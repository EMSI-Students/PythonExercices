from django.http import HttpResponse

def payment(request):
    return HttpResponse("<h1>This Page for Payment</h1>")
