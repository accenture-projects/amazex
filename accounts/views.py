from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
import os


def error_404_view(request, exception):
    return render(request, 'home/404.html')


def logout(request):
    if request.method == "GET":
        logout_auth(request)
        request.session.flush()
        messages.warning(
            request, "You have successfully been logged out of your account.")
        return redirect('home')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            curr_user = authenticate(username=username, password=password)
            if curr_user is not None:
                login_auth(request, curr_user)
                messages.success(request, 'Welcome back to staff section. ')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')

        users = User.objects.all()
        params = {
            'users': users,
        }
        return render(request, 'accounts/login.html', params)


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        username = request.POST['username']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            try:
                user = User.objects.get(username=username)
                return HttpResponse("User already exist with the username you enetered.")
            except User.DoesNotExist:
                new_user = User.objects.create_user(username, email, password=password)


                new_user.first_name = first_name
                new_user.last_name = last_name

                fullname = first_name + ' ' + last_name

                new_user.save()

                curr_user = authenticate(username=username, password=password)
                if curr_user is not None:
                    login_auth(request, curr_user)

                    messages.success(
                        request, f"Welcome to Amaze, {fullname} your account has been created "
                                 f"successfully. Now you may go ahead and create your profile.")
                    return redirect('profile')

        else:
            return HttpResponse("Invalid password")

    users = User.objects.all()
    params = {
        'users': users,
    }

    return render(request, 'accounts/signup.html', params)
