from multiprocessing import context
from operator import contains
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product


# Create your views here.


# def get_home(request):
#     return HttpResponse("<h1>HELLO<h1>")

# def get_product(request, product_number):
#     product = Product.objects.get(id=product_number)
#     return HttpResponse(f'''Your Product Id: {product.id}
#                         \n Name: {product.name}
#                         \n Price {product.price}''')

def get_home(request):
    return render(request, "home.html")


def get_product(request, product_number):
    try:

        product = Product.objects.get(id=product_number)
        context = {"product": {"name": product.name,
                               "price": product.price, "description": product.description}}
    except Product.DoesNotExist:
        # raise Http404("Product does not exist")
        raise Http404("Productt does not exist")
    return render(request, "product-detail.html", context)


def get_products(request):
    products = Product.objects.all()
    new_products = []
    for product in products:
        new_products.append({
            "name": product.name,
            "price": product.price})
    context = {"products": new_products}
    return render(request, "product-list.html", context)
