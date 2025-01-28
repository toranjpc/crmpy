from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserOption

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

admin.site.register(User, CustomUserAdmin)

class KindFilter(admin.SimpleListFilter):
    title = 'نوع' 
    parameter_name = 'kind'  

    def lookups(self, request, model_admin):
       
        return UserOption.KIND_CHOICES

    def queryset(self, request, queryset):
       
        if self.value():
            return queryset.filter(kind=self.value())
        return queryset
       
@admin.register(UserOption)
class CustomUserOption(admin.ModelAdmin):
    list_display = ('title', 'kind', 'status')

    fieldsets = (
        ('datas', {'fields': ('title', 'option', 'status')}),
    )

    add_fieldsets = (   
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'option', 'status'),
        }),
    )
    
    list_filter = (KindFilter,)  # اضافه کردن فیلتر سفارشی
    search_fields = ('user__username', 'kind')  # جستجو بر اساس نام کاربر و نوع
    
    list_per_page = 20
