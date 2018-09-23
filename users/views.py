from django.shortcuts import render, redirect
from .forms import ConnexionForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            error = "Mauvais nom d'utilisateur ou mot de passe" 
        else:
            auth_login(request, user)
            return redirect('index')

    return render(request, 'users/login.html', locals())

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CustomUserCreationForm
    return render(request, 'users/login.html', locals())

@login_required
def logout(request):
    auth_logout(request)
    return redirect('users:login')