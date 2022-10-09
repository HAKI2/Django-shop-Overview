from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from django.contrib import messages

@login_required
def orders(request):
    if not request.user.is_authenticated:
        redirect('mainpage:login')
    else:
        a = request.user.order.all()
        take = {'orders': a,
                'orders_len': len(a),
                'section': "orders",
                }
        return render(request, 'order/orders.html', context=take)

@login_required
def order_cansel(request, pk_id):
    order = Order.objects.get(id=pk_id)
    if order.paid == 'False':
        order.paid = 'Canceled'
        order.save()
    return redirect('userprofile:order:orders')

@require_POST
def create_order(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated:
            a = form.save()
            a.user = request.user
            a.save()
            for i in request.cart:
                orderitem = OrderItem(order=a, product=i['product'], price=i['product'].price, quantity=i['quantity'])
                orderitem.save()
            request.cart.flush()
            return redirect('userprofile:order:orders')
        else:
            form.save()
            return redirect('products:products')
    else:
        messages.error(request, "Something went wrong. Please try again.")
        return redirect('cart_page:checkout')


@login_required
def detail(request, pk_id):
    take = {
        'order': Order.objects.get(id=pk_id),
    }
    return render(request, 'order/detail.html', context=take)

@login_required
def order_pay(request, pk_id):
    order = Order.objects.get(id=pk_id)
    if order.paid == 'False':
        order.paid = 'True'
        order.save()
    return redirect('userprofile:order:orders')

@login_required
def order_delete(request, pk_id):
    order = Order.objects.get(id=pk_id)
    if order.paid == 'Canceled' or order.paid == 'Finished':
        order.delete()
    return redirect('userprofile:order:orders')