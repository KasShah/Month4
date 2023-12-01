from django.shortcuts import HttpResponse, render

from post.models import Product, Category, Comment


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products,
        }

        return render(request, 'products/products.html', context=context)

def post_d_view(request, post_id):
    if request.method =='GET':
        products = Product.objects.get(id=post_id)

        context = {
            'products': products
            }

        return render(request, 'products/product_detail.html', context)


def category_view(request):
    if request.method =='GET':
        categories = Category.objects.all()

        context = {
            'categories': categories,
            'name': 'Mia'
        }

        return render(
            request,
            'products/categories.html',
            context=context
        )


