from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.all()

    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)