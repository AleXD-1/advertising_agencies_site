from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            login(request, user)
            if p_form.profile_type == 'CL':
                return redirect('create_client_profile')
            else:
                return redirect('home')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'common/register.html', {'u_form': u_form, 'p_form': p_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'common/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
