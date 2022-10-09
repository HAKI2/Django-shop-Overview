from django.urls import path
from . import views

app_name = 'cart_page'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('addone/<int:pr_id>', views.addone, name='addone'),
    path('removeone/<int:pr_id>', views.removeone, name='removeone'),
    path('remove/<int:pr_id>', views.remove, name='remove'),
]