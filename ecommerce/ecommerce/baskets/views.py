from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ecommerce.products.forms import AddProductToBasketForm
from ecommerce.products.models import Product


def add_product_to_basket(request, slug):
    product = get_object_or_404(Product, slug=slug)

    form = AddProductToBasketForm(min(product.stock, 10), request.POST)

    if form.is_valid():
        quantity = int(form.cleaned_data['quantity'])
        request.basket.add(product, quantity)
        messages.success(request, f'You added {quantity} x {product.name} to your ')
        return redirect(reverse('products:product details', kwargs={'slug': product.slug}))
    else:
        context = {
            'product': product,
            'form': form,
        }
        return render(request, 'products/product_details.html', context)
