from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='start'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.Shop.as_view(), name='shop'),
    #path('product/<str:slug>', views.GetProduct.as_view(), name='product'),
    path('product/<str:slug>', views.product_detail, name='product'),
    path('category/<str:slug>', views.ProductByCategory.as_view(), name='category'),
    path('subcategory/<str:slug>',
         views.ProductBySubcategory.as_view(), name='subcategory'),
    path('search/', views.Search.as_view(), name='search'),
]
