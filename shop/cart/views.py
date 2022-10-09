from django.shortcuts import render, redirect
from products.models import Product
from order.forms import OrderForm

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'cart/checkout.html', context={"form": OrderForm()})

def changequantity(request, pr_id, quantity):
    request.cart.add(product=pr_id, quantity=quantity)
    return redirect('cart_page:cart')

def remove(request, pr_id):
    request.cart.remove(product=Product.objects.get(id=pr_id))
    return redirect('cart_page:cart')

def addone(request, pr_id):
    request.cart.add(product=Product.objects.get(id=pr_id), quantity=1)
    return redirect('cart_page:cart')

def removeone(request, pr_id):
    request.cart.add(product=Product.objects.get(id=pr_id), quantity=-1)
    return redirect('cart_page:cart')