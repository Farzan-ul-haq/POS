from django.shortcuts import render, redirect

from .forms import ProductForm
# Create your views here.

def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'product/create.html')
