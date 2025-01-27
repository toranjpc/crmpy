from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .user_model import User
import re


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Password"))
    remember_me = forms.BooleanField(required=False)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='نام')
    last_name = forms.CharField(max_length=30, required=True, label='نام خانوادگی')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('این نام کاربری قبلاً استفاده شده است.')
        
        # بررسی اینکه آیا نام کاربری قالب شماره موبایل دارد
        if re.match(r'^\+?1?\d{9,15}$', username):
            # اگر نام کاربری شماره موبایل است، آن را در فیلد موبایل نیز ذخیره کنید
            self.cleaned_data['phone_number'] = username
            
        return username
        
