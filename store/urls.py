from django.urls import path

from store.views import product_all, product_detail, category_list, search

app_name = 'store'
urlpatterns = [
    path('', product_all, name='product_all'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),
    path('item/search/<str:product_title>/', search, name='search'),
]
