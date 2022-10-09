from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'telephone_number', 'address_region', 'address_city', 'address_address',
                  'address_flat', 'address_zip']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
            }),
            'telephone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 000 000-00-00'
            }),
            'address_region': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Moscow region',
            }),
            'address_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Moscow',
            }),
            'address_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Street, house',
            }),
            'address_flat': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '123',
            }),
            'address_zip': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '123456',
            }),
        }
        labels = {
            'address_region': 'Region/Area',
            'address_city': 'City',
            'address_address': 'Address',
            'address_flat': 'Flat',
            'address_zip': 'Zip code',
        }