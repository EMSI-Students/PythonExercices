from django.urls import path
from .views import firstPageView

urlpatterns = [
    path('first/', firstPageView, name='first_page'),
]
