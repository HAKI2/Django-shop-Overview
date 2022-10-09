from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('<int:pk_id>/', views.detail, name='detail'),
    path('order_cancel/<int:pk_id>', views.order_cansel, name='order_cancel'),
    path('order_delete/<int:pk_id>', views.order_delete, name='order_delete'),
    path('order_pay/<int:pk_id>', views.order_pay, name='order_pay'),
]