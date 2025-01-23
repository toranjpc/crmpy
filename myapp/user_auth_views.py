from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', block=True)
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
