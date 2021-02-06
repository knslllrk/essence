from django import template
from shop.models import Category, Subcategory


register = template.Library()


@register.inclusion_tag('shop/menu_tpl.html')
def show_menu(menu_class='megamenu'):
    categories1 = Category.objects.get(name="Men's")
    categories2 = Category.objects.get(name="Women's")
    categories3 = Category.objects.get(name="Kid's")
    subcategories1 = Subcategory.objects.filter(category=categories1)
    subcategories2 = Subcategory.objects.filter(category=categories2)
    subcategories3 = Subcategory.objects.filter(category=categories3)
    return {"categories1": categories1, "subcategories1": subcategories1, "categories2": categories2, "subcategories2": subcategories2, "categories3": categories3, "subcategories3": subcategories3, "menu_class": menu_class}
