from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model
)
from .forms import CustomUserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        user_creation_form = CustomUserCreationForm()

    context = {
        'user_creation_form': user_creation_form
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        authentication_form = AuthenticationForm(request, request.POST)

        if authentication_form.is_valid():
            auth_login(request, authentication_form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        authentication_form = AuthenticationForm()

    context = {
        'authentication_form': authentication_form
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, username):
    person = get_user_model().objects.get(username=username)
    
    context = {
        'person': person,
    }
    
    return render(request, 'profile.html', context)
