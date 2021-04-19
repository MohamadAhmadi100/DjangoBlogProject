from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{user} عزیز خوش آمدید")
                return redirect("blog:blog_home")
            else:
                messages.error(request, "نام کاربری یا رمز عبور نادرست است", "danger")
                form = UserLoginForm()

    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, f"{request.user.username} شما با موفقیت خارج شدید")
    return redirect("blog:blog_home")


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # if User.objects.get(username=cd['username']):
            #     messages.error(request, 'کاربری با این نام موجود است', 'danger')
            #     form = UserRegistrationForm()
            # else:
            try:
                User.objects.create_user(cd['username'], cd['email'], cd['password1'])
                messages.success(request, f"{cd['username']} عزیز ثبت نام شما با موفقیت انجام شد")
                return redirect("accounts:user_login")
            except:
                messages.error(request, 'کاربری با این نام موجود است', 'danger')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
