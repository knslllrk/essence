from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from shop.models import Category


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    categories1 = Category.objects.get(name="Men's")
    categories2 = Category.objects.get(name="Women's")
    categories3 = Category.objects.get(name="Kid's")
    return render(request, 'shop/index.html', {"categories1": categories1, "categories2": categories2, "categories3": categories3})


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            messages.success(
                request, 'Congratulations! You have successfully registered')
            new_user = user_form.save()
            profile = Profile.objects.create(user=new_user)
            return redirect('login')
        else:
            messages.error(request, 'Registration error')
    else:
        user_form = UserRegisterForm()
    return render(request, 'account/register.html', {"user_form": user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Congratulations! Your profile has been successfully updated')
            return redirect('dashboard')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
