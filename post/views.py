from django.shortcuts import HttpResponse, render

from post.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(request, 'products/products.html')