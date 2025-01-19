from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User  # فرض کنید مدل User در فایل models.py تعریف شده است
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['username', 'email', 'mobile']
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_form.html'
    fields = ['username', 'email', 'mobile']
    success_url = reverse_lazy('user_list')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        # اگر درخواست POST باشد، فرم را با داده‌های ارسال شده پر کنید
        form = SignUpForm(request.POST)
        if form.is_valid():
            # اگر فرم معتبر باشد، کاربر را ذخیره کنید
            user = form.save()
            # کاربر را وارد سیستم کنید (اختیاری)
            login(request, user)
            # کاربر را به صفحه‌ای دیگر هدایت کنید (مثلاً صفحه اصلی)
            return redirect('home')  # تغییر 'home' به نام URL مورد نظر
    else:
        # اگر درخواست GET باشد، یک فرم خالی نمایش دهید
        form = SignUpForm()
    
    # فرم را به تمپلیت ارسال کنید
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # پس از لاگین، کاربر به صفحه اصلی هدایت می‌شود
            # else:
            #     return JsonResponse(request.POST)
            #     return username

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})