from django.urls import path
from .views import firstPageView

urlpatterns = [
    path('', firstPageView, name='home'),
]
