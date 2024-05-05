from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from product.models import Product,Images,Category
from.models import * 
from django.contrib import messages
from ecomapp.forms import SearchForm 
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



def About(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={
        'setting':setting,
        'category': category,
    }
    return render(request,'about.html',context)


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Profile details updated.')

            return redirect('contact_dat')
        
    setting = Setting.objects.get(id=1)
    form = ContactForm
    category = Category.objects.all()
    context = {
        'setting':setting,
        'form': form,
        'category': category,
    }
    return render(request, 'contact_form.html', context)


 

def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            sliding_images = Product.objects.all().order_by('id')[:2]
            setting = Setting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'sliding_images': sliding_images,
                'setting': setting,
            }
            return render(request, 'category_product.html', context)
    return HttpResponseRedirect('category_product')

       



def product_single(request,id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images= Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]

    context={
        'category': category,
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
     }
    return render(request,'product_single.html',context)


def category_product(request,id,slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding = Product.objects.all().order_by('id')[:2]
    product_cat = Product.objects.filter(category_id=id)

    context={
        'category':category,
        'setting': setting,
        'product_cat': product_cat,
        'sliding': sliding,
    }
    return render(request,'category_product.html',context)
