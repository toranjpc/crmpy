from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import LoginForm, SignUpForm

from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', block=False)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(8644*30)  
                else:
                    request.session.set_expiry(0)
                return redirect('dashboard')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
                return redirect('login') 
    else:
        form = LoginForm()
    return render(request, 'dashboard/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  

@ratelimit(key='ip', rate='5/m', block=False)
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if hasattr(form, 'cleaned_data') and 'phone_number' in form.cleaned_data:
                user.phone_number = form.cleaned_data['phone_number']
            user.save()
            login(request, user)
            messages.success(request, _('ثبت‌نام شما با موفقیت انجام شد!'))
            return redirect('home')  
        else:
            messages.error(request, _('خطا در ثبت‌نام. لطفاً اطلاعات را بررسی کنید.'))
    else:
        form = SignUpForm()
    return render(request, 'dashboard/signup.html', {'form': form})