from itertools import product
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product
# Create your views here.

def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            print('saved')
            form.save()
            return redirect('/')
        print(form.errors)
    return render(request, 'product/create.html', {
        'form': form
    })

def update(request, pr_id):
    p = Product.objects.get(id=pr_id)
    form = ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'product/update.html', {
        'form': form
    })

def delete(request, pr_id):
    Product.objects.get(id=pr_id).delete()
    return redirect('/')