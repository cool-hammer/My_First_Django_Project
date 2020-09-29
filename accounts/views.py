from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('articles:index')
    else:
        user_creation_form = UserCreationForm()

    context = {
        'user_creation_form': user_creation_form
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        authentication_form = AuthenticationForm(request, request.POST)
        
        if authentication_form.is_valid():
            auth_login(request, authentication_form.get_user())
            return redirect('articles:index')
    else:
        authentication_form = AuthenticationForm()
        
    context = {
        'authentication_form': authentication_form
    }
    
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')