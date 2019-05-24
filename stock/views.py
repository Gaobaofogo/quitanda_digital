from django.shortcuts import render

from .forms import ProductForm
from .models import Product


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def product_list(request):
    products = Product.objects.all()

    return render(request, 'stock/product_list.html', {'products': products})


def product_add(request):
    form = ProductForm()
    context = {}

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            context['success'] = True

    context['form'] = form

    return render(request, 'stock/product_add.html', context)
