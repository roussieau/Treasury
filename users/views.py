from django.shortcuts import render
from .forms import ConnexionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            error = "Mauvais nom d'utilisateur ou mot de passe" 

    return render(request, 'users/login.html', locals())

@login_required
def logout(request):
    return render(request, 'users/logout.html', locals())

