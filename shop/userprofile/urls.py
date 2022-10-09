from django.urls import path, include
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', include('order.urls'), name='order'),
    path('settings/', views.settings, name='settings'),
    path('favourite/', views.favourite, name='favourite'),
]