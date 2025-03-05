from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User, UserOption
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
# from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Permission
from django.forms.models import model_to_dict
from django.urls import reverse
from jdatetime import date as jdate
from datetime import datetime
from django.utils import timezone
import json

# simpleFront Start
def home(request):
    product_range = range(10)  # ایجاد لیست از 0 تا 9
    return render(request, 'catalog/index.html', {'product_range': product_range})

# simpleFront End




# dashboard Start
@login_required
def dashboard(request):
    # translation.activate('fa')
    # request.LANGUAGE_CODE = 'fa'
    
    users = User.objects.all()
    return render(request, 'dashboard/dashboard.html', {'datas': {'users':users}})

# dashboard End




# Userse Start

# User Category Start
@login_required
def User_Category_list(request):
    filters = Q()
    if request.GET.get('id'):
        try:
            user_id = int(request.GET.get('id'))
            filters |= Q(id=user_id)
        except ValueError:
            pass  

    if request.GET.get('name'):
        name = request.GET.get('name')
        filters |= Q(title__icontains=name)

    filters &= Q(kind='UserCategory')
    fields = ['id', 'title','option','status','created_at']
    queryset=UserOption.objects.values(*fields).filter(filters)

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10) 
    try:
        UserOptions = paginator.page(page)
    except PageNotAnInteger:
        UserOptions = paginator.page(1)
    except EmptyPage:
        UserOptions = paginator.page(paginator.num_pages)


    permissions = Permission.objects.select_related('content_type').order_by('content_type_id')
    # گروه‌بندی permissions بر اساس content_type
    grouped_permissions = {}
    for perm in permissions:
        content_type = perm.content_type.model
        if content_type not in grouped_permissions:
            grouped_permissions[content_type] = {
                'model': content_type,
                'verbose_name': perm.content_type.name,
                'permissions': []
            }
        
        grouped_permissions[content_type]['permissions'].append({
            'id': perm.id,
            'name': perm.name,
            'codename': perm.codename
        })
        
    return render(request, 'dashboard/User_Kind_List.html', {'UserOptions': UserOptions,'request':request,'permissions':grouped_permissions})

# @csrf_exempt
@login_required
def User_Category_Add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        permissions = request.POST.getlist('permissions[]')

        option = {'form':request.POST.get('option'),
                'permissions': ','.join(permissions) if permissions else '',
                }
        kind = 'UserCategory'
        status = request.POST.get('status', 0)
        
        if not title:
            messages.error(request, 'خطا!!! لطفا فیلد های مورد نیاز را تکمیل نمایید')
            return redirect('User_Kind_list')

        if not status:
            status = 0
        
        UserOption.objects.create(
            title=title, option=option, kind=kind, status=status
        )
        messages.success(request, 'عملیات با موفقیت انجام شد.')
        return redirect('User_Kind_list')

@login_required
def User_Category_Edit(request, id):
    user_option = get_object_or_404(UserOption, id=id)

    if request.resolver_match.url_name == 'User_Kind_View':
        user_option_data = model_to_dict(user_option)
        return JsonResponse(user_option_data)
    
    elif request.method == 'POST':


        title = request.POST.get('title')
        option = user_option.option or {}
        option['form'] = request.POST.get('option')
        permissions = request.POST.getlist('permissions[]')
        option['permissions'] = ','.join(permissions) if permissions else ''
        # kind = 'UserCategory'
        status = request.POST.get('status', 0)
        
        if not title:
            messages.error(request, 'خطا!!! لطفا فیلد های مورد نیاز را تکمیل نمایید')
            return redirect('User_Kind_list')

        if not status:
            status = 0
        
        user_option.title = title
        user_option.option = option
        # user_option.kind = kind
        user_option.status = status
        user_option.save()
        
        messages.success(request, 'بروززسانی با موفقی انجام شد.')
        return redirect('User_Kind_list')

    return HttpResponse(status=404)


@login_required
def User_Category_Destroy(request, id):
    count=0

    filters = Q(kind=id)
    count += User.objects.filter(filters).count()

    if count == 0:
        filters = Q(id=id)
        UserOption.objects.filter(filters).delete()
        messages.warning(request, 'دسته بندی با موفقیت حذف شد.')
    else:
        messages.error(request, 'امکان حذف وجود ندارد. کاربرانی با این دسته بندی وجود دارند.')

    return redirect('User_Kind_list')

# User Category End

# User Category Start
@login_required
def User_Group_list(request):
    filters = Q()
    if request.GET.get('id'):
        try:
            user_id = int(request.GET.get('id'))
            filters |= Q(id=user_id)
        except ValueError:
            pass  

    if request.GET.get('name'):
        name = request.GET.get('name')
        filters |= Q(title__icontains=name)

    filters &= Q(kind='UserGroup')
    fields = ['id', 'title','option','status','created_at']
    queryset=UserOption.objects.values(*fields).filter(filters)

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10) 
    try:
        UserOptions = paginator.page(page)
    except PageNotAnInteger:
        UserOptions = paginator.page(1)
    except EmptyPage:
        UserOptions = paginator.page(paginator.num_pages)

    # return JsonResponse({
    #     'permissions': list(grouped_permissions.values())
    # })
    
    return render(request, 'dashboard/User_Groups_List.html', {'UserOptions': UserOptions,'request':request})

# @csrf_exempt
@login_required
def User_Group_Add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        
        option = {
            'form': request.POST.get('option'),
        }
        kind = 'UserGroup'
        status = request.POST.get('status', 0)
        
        if not title:
            messages.error(request, _('Error: Please fill in all required fields'))
            return redirect('User_Group_list')

        if not status:
            status = 0
        
        UserOption.objects.create(
            title=title, option=option, kind=kind, status=status
        )
        messages.success(request, _('Data updated successfully'))
        return redirect('User_Group_list')

@login_required
def User_Group_Edit(request, id):
    user_option = get_object_or_404(UserOption, id=id)
    
    if request.resolver_match.url_name == 'User_Group_View':
        user_option_data = model_to_dict(user_option)
        return JsonResponse(user_option_data)
    
    elif request.method == 'POST':

        title = request.POST.get('title')
        if not title:
            messages.error(request, _('Error: Please fill in all required fields'))
            return redirect('User_Group_list')
        
        option = user_option.option or {}
        option['form'] = request.POST.get('option')
        status = bool(request.POST.get('status'))
        
        user_option.title = title
        user_option.option = option
        user_option.status = status
        user_option.save()
        
        messages.success(request, _('Data updated successfully'))
        return redirect('User_Group_list')
    
    return HttpResponse(status=404)

@login_required
def User_Group_Destroy(request, id):
    count = 0

    filters = Q(kind=id)
    count += User.objects.filter(filters).count()

    if count == 0:
        filters = Q(id=id)
        UserOption.objects.filter(filters).delete()
        messages.warning(request, _('Data deleted successfully'))
    else:
        messages.error(request, _('Cannot delete group. Users with this group exist.'))

    return redirect('User_Group_list')

# User Category End



@login_required
def Users_list(request):
    filters = Q()
    if request.GET.get('id'):
        try:
            user_id = int(request.GET.get('id'))
            filters |= Q(id=user_id)
        except ValueError:
            pass  

    if request.GET.get('name'):
        name = request.GET.get('name')
        filters |= Q(first_name__icontains=name) | Q(last_name__icontains=name)

    if request.GET.get('mobile'):
        mobile = request.GET.get('mobile')
        filters |= Q(mobile__icontains=mobile)

    if request.GET.get('email'):
        email = request.GET.get('email')
        filters |= Q(email__icontains=email)

    if request.GET.get('UserCategory') and request.GET.get('UserCategory')!='All':
        UserCategory = request.GET.get('UserCategory')
        filters |= Q(kind=UserCategory)

    fields = ['id', 'first_name', 'last_name','username', 'mobile', 'kind','date_joined']
    queryset = User.objects.values(*fields).filter(filters)

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10) 
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    UOfilters = Q(kind='UserCategory')
    UOfields = ['id', 'title']
    UserOptions=UserOption.objects.values(*UOfields).filter(UOfilters)

    return render(request, 'dashboard/User_List.html', {'users': users, 'UserOptions':UserOptions, 'request':request})


@login_required
def User_Add_Edit(request, id=0):
    # if request.resolver_match.url_name == 'User_Group_View':

    if request.method == 'GET':
        UOfilters = Q(kind='UserCategory')
        UOfields = ['id', 'title']
        UserOptions=UserOption.objects.values(*UOfields).filter(UOfilters)

        UGfilters = Q(kind='UserGroup')
        UGfields = ['id', 'title']
        UserGroups=UserOption.objects.values(*UGfields).filter(UGfilters)
   
        filters = Q(id=id)
        user = User.objects.select_related('kind').prefetch_related('groups').filter(filters).first()

        # user_data = model_to_dict(user)
        # user_data['groups'] = model_to_dict(user.groups) if user.groups else None
        # return JsonResponse(user_data)
        

        selectedLink = reverse('User_Add')     
    
        return render(request, 'dashboard/User_View.html', 
                      {'selectedLink':selectedLink,
                       'UserOptions':UserOptions,
                        'UserGroups':UserGroups,
                        'pageTitle':'user add',
                        'User':user,
                        # 'selected_groups_ids': selected_groups_ids
                        }
        )

    elif request.method == 'POST':

        # if not id: 
        #     user = User()
        # else:  
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            messages.error(request, 'کاربر مورد نظر یافت نشد')
            return redirect('Users_list')
        
        user.sex = request.POST.get('sex')
        user.kind_id = request.POST.get('kind')
        user.alias = request.POST.get('alias')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.mobile = request.POST.get('mobile')
        user.email = request.POST.get('email')
        user.ircode = request.POST.get('ircode')
        user.username = request.POST.get('userusernamename')
        # if request.POST.get('userpassword') and request.POST.get('userpassword') != '000':
        #     user.set_password(request.POST.get('userpassword'))
        
        try:
            if request.POST.get('birth'):
                shamsi_date = request.POST.get('birth').split('/')
                if len(shamsi_date) == 3:
                    year, month, day = map(int, shamsi_date)
                    miladi_date = jdate(year, month, day).togregorian()
                    user.birth = datetime.combine(miladi_date, datetime.min.time())
                else:
                    user.birth = timezone.now()
            else:
                user.birth = timezone.now()
        except Exception as e:
            user.birth = timezone.now()

        user_kind_data = {}
        for key in request.POST:
            if key.startswith('UserKindData_'):
                field_name = key[13:]
                values = request.POST.getlist(key)
                values = [v for v in values if v.strip()]
                if values:
                    user_kind_data[field_name] = values
        
        user.des = user.des or {}
        user.des['UserKindData'] = user_kind_data
    
        user.des['des'] = request.POST.get('userDes')

        # return JsonResponse({
        #     'data': dict(user_kind_data),
        #     'files': dict(request.FILES)
        # })

        user.save()
        
        user.groups.clear()
        for group_id in request.POST.getlist('Categores[]'):
            user.groups.add(group_id)
        
        messages.success(request, 'کاربر با موفقیت ذخیره شد')
        return redirect('User_Edit', id=user.id)


@login_required
def User_View(request, id):
    user = get_object_or_404(User, id=id)
    # return HttpResponse(user)
    return render(request, 'dashboard/User_View.html', {'user': user})

@login_required
def User_Copy(request, id):
    return HttpResponse(id)


@login_required
def User_Edit(request, id):
    return HttpResponse(id)


@login_required
def User_Destroy(request, id):
    return HttpResponse(id)

# Userse End

