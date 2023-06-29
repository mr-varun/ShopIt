from django.urls import path
from django.contrib import admin
from .views import product_list


urlpatterns = [
    path('', product_list, name='product_list'), #index
]