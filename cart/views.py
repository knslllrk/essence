from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, update_quantity=cd['update'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
