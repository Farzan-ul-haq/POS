import json

from django.shortcuts import render

from category.models import Category
# Create your views here.

def index(request):
    category = Category.objects.all()
    if not 'order_items' in request.session:
        print('cart created')
        order_items = {'total_price': 0}
        request.session['order_items'] = json.dumps(order_items)
    order_data = json.loads(request.session['order_items'])
    total_price = order_data.pop('total_price')
    return render(request, 'core/index.html', {
        'categories': category,
        'order_data': order_data,
        'total_price': total_price
    })