from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'user_register'),
    path('login/', views.login, name = 'user_login'),
    path('change-password/', views.change_password, name = 'user_change_password'),
    path('hello/', views.hello, name = 'user_hello'),
    path('hello/<str:user_name>/', views.hello, name = 'user_hello'),
    path('hello/<user_name>/<int:user_age>/', views.hello, name='user_age'),
]
