from decimal import Decimal
from products.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        self.cart = request.session.get('cart', {})

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if quantity > 0:
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity': 0,
                                         }
            self.cart[product_id]['quantity'] += quantity
            self.save()
        else:
            self.cart[product_id]['quantity'] += quantity
            if self.cart[product_id]['quantity'] <= 0:
                self.remove(product)
            self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            a = str(item['product'].price)[::-1]
            item['total_price'] = str(item['product'].price * item['quantity'])[::-1]
            item['price'] = ' '.join([a[i:i + 3] for i in (0, len(a), 3)])[::-1]
            item['total_price'] = ' '.join([item['total_price'][i:i + 3] for i in (0, len(item['total_price']), 3)])[::-1]
            yield item

    def len(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        return sum(Decimal(item['product'].price) * item['quantity'] for item in
                   self.cart.values())

    def get_total_price_str(self):
        a = str(self.get_total_price())[::-1]
        return ' '.join([a[i:i+3] for i in (0, len(a), 3)])[::-1]

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def flush(self):
        del self.cart
        del self.session['cart']
