from django.shortcuts import render, redirect

from Products.forms import ProductCreateForm, ReviewCreateForm
from Products.models import Product, Review


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        form = ReviewCreateForm()
        product = Product.objects.get(id=id)
        context = {
            'product': product,
            'comments': product.review_set.all(),
            'form': form
        }
        return render(request, 'products/detail.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ReviewCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=form.cleaned_data.get('product')

            )

            return redirect('/products')

        return render(request, 'products/detail.html', context={'form': form})


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)
        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={'form': form})
