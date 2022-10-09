from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

class UserLoginForm(AuthenticationForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control rounded-4", "type": "password", "placeholder": "Password", }),
    )
    username = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={"class": "form-control rounded-4", "placeholder": "Email", }))

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Your name',
                               widget=forms.TextInput(attrs={"class": "form-control rounded-4", "placeholder": "Your name",
                                                                               }))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={"class": "form-control rounded-4", "placeholder": "Email",}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control rounded-4", "type": "password", "placeholder": "Password",}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-control rounded-4", "placeholder": "Password confirmation",}),
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def clean_username(self):
        return self.cleaned_data['username']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user