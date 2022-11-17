from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.http import HttpResponse


def search(request, product_title):
    products = Product.objects.filter(title=product_title)

    return render(request, 'store/products/search.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_all(request):
    products = Product.products.all()
    lst = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    return render(request, 'store/home.html', {'products': page_obj })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

def get_pro(request):
    pass