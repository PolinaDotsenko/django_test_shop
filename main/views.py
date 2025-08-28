from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)   #выводятся только доступные продукты
    
    category = None
    if category_slug:
        category = get_object_or_404(Category, categoty_slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'main/product/list.html',        #templates не указываем, потому что 
                  {'category': category,                    #render по умолчаию будет искать в папке templates
                   'categories': categories, 
                   'products': products})