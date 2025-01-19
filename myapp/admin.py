from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # فیلدهایی که در لیست کاربران نمایش داده می‌شوند
    list_display = ('first_name', 'last_name', 'mobile', 'date_joined', 'is_active')

    # فیلدهایی که در صفحه ویرایش کاربر نمایش داده می‌شوند
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'mobile', 'ircode', 'birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # فیلدهایی که در صفحه اضافه کردن کاربر نمایش داده می‌شوند
    add_fieldsets = (   
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','username', 'email', 'mobile', 'password1', 'password2'),
        }),
    )

# ثبت مدل User با کلاس ادمین سفارشی
admin.site.register(User, CustomUserAdmin)