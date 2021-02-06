from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Subcategory
from django.db.models import F
from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404


def index(request):
    categories1 = Category.objects.get(name="Men's")
    categories2 = Category.objects.get(name="Women's")
    categories3 = Category.objects.get(name="Kid's")
    return render(request, 'shop/index.html', {"categories1": categories1, "categories2": categories2, "categories3": categories3})


def contact(request):
    return render(request, 'shop/contact.html')


class Shop(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ProductByCategory(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'], available=True)


class ProductBySubcategory(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(subcategory__slug=self.kwargs['slug'], available=True)


'''class GetProduct(DetailView):
    model = Product
    template_name = 'shop/single.html'
    context_object_name = 'product'

    ### Разобраться что это значит ###
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context'''


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    views = product.views = F('views') + 1
    product.save()
    return render(request, 'shop/single.html', {'product': product, 'cart_product_form': cart_product_form})


class Search(ListView):
    template_name = 'shop/search.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('search'), available=True)
