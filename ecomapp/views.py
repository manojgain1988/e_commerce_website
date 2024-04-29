from django.shortcuts import render
from product.models import Product
from.models import *

# Create your views here.

def Home(request):
    setting = Setting.objects.get(id=1)
    sliding = Product.objects.all().order_by('id')[:3]
    latest_products = Product.objects.all().order_by('-id')
    feature_products = Product.objects.all()
    
    context={
        'setting': setting,
        'sliding': sliding,
        'latest_products': latest_products,
        'feature_products': feature_products,
    }
    return render(request,'home.html',context)