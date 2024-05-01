from django.shortcuts import render,HttpResponse
from product.models import Product,Images,Category
from.models import *

# Create your views here.

def Home(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding = Product.objects.all().order_by('id')[:3]
    latest_products = Product.objects.all().order_by('-id')
    feature_products = Product.objects.all()
    
    context={
        'category': category,
        'setting': setting,
        'sliding': sliding,
        'latest_products': latest_products,
        'feature_products': feature_products,
        
        
    }
    return render(request,'home.html',context)



def product_single(request,id):
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images= Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]

    context={
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
     }
    return render(request,'product_single.html',context)


def category_product(request,id,slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding = Product.objects.all().order_by('id')[:3]
    product_cat = Product.objects.filter(category_id=id)

    context={
        'category':category,
        'setting': setting,
        'sliding': sliding,
        'product_cat':product_cat
    }
    return render(request,'category_product.html',context)
