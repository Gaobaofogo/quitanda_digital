from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from .forms import ProductForm
from .models import Product


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
@permission_required('stock.view_product')
def product_list(request):
    products = Product.objects.all()

    return render(request, 'stock/product_list.html', {'products': products})


@login_required
@permission_required('stock.add_product')
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
