from django.http import HttpResponse

def firstPageView(request):
    return HttpResponse('Notre première page')
