from django.shortcuts import render
from product.models import Product
from.models import *

# Create your views here.

def Home(request):
    setting = Setting.objects.get(id=1)
    sliding = Product.objects.all().order_by('id')[:3]
    context={
        'setting': setting,
        'sliding': sliding,
    }
    return render(request,'home.html',context)