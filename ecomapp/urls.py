from django.urls import path
from .views import Home, product_single,category_product




urlpatterns = [
    path('', Home, name='home'),
    path('product/<int:id>/', product_single, name='product_single'),
    path('product/<int:id>/<slug:slug>/', category_product, name='category_product'),
] 