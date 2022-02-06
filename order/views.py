import json

from django.shortcuts import render, redirect

from product.models import Product
from order.models import Order
# Create your views here.

def add(request, pr_id):
    p = Product.objects.get(id=pr_id)
    data = json.loads(request.session['order_items'])
    if p.name in data:
        data[p.name] += 1
    else:
        data[p.name] = 1
    data['total_price'] += p.price
    request.session['order_items'] = json.dumps(data)
    return redirect('/')

def empty(request):
    request.session['order_items'] = json.dumps({'total_price': 0})
    return redirect('/')

def submit(request):
    Order.objects.create(
        products = request.session['order_items']
    )
    return empty(request)

def list(request):
    return render(request, 'order/list.html', {
        'orders': Order.objects.all().order_by('-id')
    })