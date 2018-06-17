from django.shortcuts import render, get_object_or_404

from Products.models import Product, Category


def detail_product(request, name_url):
    product = get_object_or_404(Product, name_url=name_url)
    return render(request, 'product.html', locals())


def category_detail(request, category_name_url):
    category = Category.objects.get(name_url=category_name_url)
    products = Product.objects.filter(category=category.id)
    return render(request, 'category_detail.html', locals())


def category_list(request):
    return render(request, 'categories.html')
