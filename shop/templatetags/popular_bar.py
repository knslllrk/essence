from django import template
from shop.models import Product


register = template.Library()


@register.inclusion_tag('shop/popular_products_tpl.html')
def get_popular(cnt=7):
    products = Product.objects.order_by('-views')[:cnt]
    return {"products": products}
