from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator


def products(request):
    paginator = Paginator(Product.objects.all(), 12)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    take = {"categorys": Category.objects.all(),
            "page_obj": page_obj,
            "page_range": paginator.page_range,
            "page": paginator.page(number=page_num),
            }
    return render(request, 'products/products.html', context=take)

def products_cat(request, category):
    a = Category.objects.get(category=category)
    paginator = Paginator(Product.objects.all().filter(category_id=a.id), 12)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    take = {"categorys": Category.objects.all(),
            "page_obj": page_obj,
            "category": category,
            "page_range": paginator.page_range,
            "page": paginator.page(number=page_num),
            }
    return render(request, 'products/products.html', context=take)

def detail(request, pr_id):
    categorys = Category.objects.all()
    product = Product.objects.get(id=pr_id)
    take = {
            "product": product,
            "categorys": categorys,
            }
    if request.method == "POST":
        request.cart.add(product, quantity=1)
    return render(request, 'products/detail.html', context=take)



