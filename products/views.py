from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def get_home(request):
    return HttpResponse("HELLO")


def get_product(request):
    product = Product.objects.get(id=1)
    return HttpResponse(f" your order is {product}")
