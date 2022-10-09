from django.db import models
from products.models import Product
from mainpage.models import User

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=30)
    address_region = models.CharField(max_length=50)
    address_city = models.CharField(max_length=200)
    address_address = models.CharField(max_length=100)
    address_flat = models.IntegerField()
    address_zip = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.CharField(default=False, max_length=20, choices=(('paid', True),
                                                                   ('not_paid', False),
                                                                   ('canceled', 'Canceled'),
                                                                   ('finished', 'Finished'),
                                                                   ))

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_cost_str(self):
        a = str(int(self.get_total_cost()))[::-1]
        return ' '.join([a[i:i + 3] for i in (0, len(a), 3)])[::-1]

    def get_all_products(self):
        return self.items.all()

    def len(self):
        return len(self.items.all())

    def __str__(self):
        return f'№{self.id}, {self.email}, {self.created.date()}, {self.paid}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_price_str(self):
        a = str(int(self.price))[::-1]
        return ' '.join([a[i:i + 3] for i in (0, len(a), 3)])[::-1]

    def get_cost(self):
        return self.price * self.quantity

    def get_cost_str(self):
        a = str(int(self.get_cost()))[::-1]
        return ' '.join([a[i:i + 3] for i in (0, len(a), 3)])[::-1]
