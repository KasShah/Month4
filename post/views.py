from django.shortcuts import HttpResponse, render, redirect

from post.models import Product, Category, Comment
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm

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

def product_create(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context)
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data['title'],
                about=form.cleaned_data['about'],
                photo=form.cleaned_data['photo'],
                rate=form.cleaned_data['rate']
            )
            return redirect('/products/')

        context = {
            'form': ProductCreateForm
        }

        return redirect('products/create.html', context)


def category_create(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForm
        }
        return render(request, 'products/create_category.html', context)

    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data['title']
            )
            return redirect('/categories/')

    context = {
        'form': CategoryCreateForm
    }

    return redirect('products/create_category.html', context)

def review_create(request):
    if request.method == 'GET':
        context = {
            'form': ReviewCreateForm
        }
        return render(request, 'products/product_detail.html', context)

    if request.method == "POST":
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                title=form.cleaned_data['title']
            )
            return redirect('/product/<int:post_id>/')

    context = {
        'form': ReviewCreateForm
    }

    return redirect('products/product_detail.html', context)
