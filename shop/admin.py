from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug',
                    'subcategory', 'price', 'available', 'created', 'updated', 'views')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ['available', 'created',
                   'updated', 'category', 'subcategory']
    list_editable = ['price', 'available']
    readonly_fields = ('views', 'created', 'updated')
    fields = ('name', 'slug', 'category', 'subcategory', 'description', 'brand',
              'price', 'available', 'image', 'image_hover', 'views', 'created', 'updated')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'category',)
    list_filter = ['category', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
