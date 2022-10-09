from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def main(request):
        return render(request, 'mainpage/main.html')



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('products:products')
        else:
            messages.error(request, "Your email and password didn't match. Please try again.")
            return render(request, 'mainpage/login.html', context={"form": UserLoginForm()})
    else:
        return render(request, 'mainpage/login.html', context={"form": UserLoginForm()})



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainpage:login')
        else:
            messages.error(request, 'ошибка регистрации')
            return render(request, 'mainpage/register.html', context={"form": CustomUserCreationForm()})
    else:
        form = CustomUserCreationForm()
        return render(request, 'mainpage/register.html', context={"form": form})

def logout(request):
    auth_logout(request)
    return redirect('products:products')