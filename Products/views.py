from django.shortcuts import render, redirect

from Products.forms import ProductCreateForm, ReviewCreateForm
from Products.models import Product, Review
from Products.constant import PAGINATION_LIMIT


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__()/PAGINATION_LIMIT
        if round(max_page)<max_page:
            max_page = round(max_page)+1
        else:
            max_page = round(max_page)
        if search:
            products = products.filter(title__icontains=search) | products.filter(description__icontains=search)
        products = products[PAGINATION_LIMIT*(page-1): PAGINATION_LIMIT*page]
        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
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
        product = Product.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                rate=form.cleaned_data.get('rate'),
                product=product

            )
            return redirect(f'/products/{id}')

        context = {
            'product': product,
            'form': form
        }
        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm,
            'user': request.user
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
