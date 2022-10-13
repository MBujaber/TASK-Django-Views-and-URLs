from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def get_home(request):
    return HttpResponse("<h1>HELLO<h1>")


def get_product(request, product_number):
    product = Product.objects.get(id=product_number)
    return HttpResponse(f'''Your Product Id: {product.id}
                        \n Name: {product.name}
                        \n Price {product.price}''')
