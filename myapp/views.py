from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User, UserOption
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Permission


# simpleFront Start
def home(request):
    return render(request, 'front/index.html', {'datas': []})

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

    return render(request, 'dashboard/User_Kind_List.html', {'UserOptions': UserOptions,'request':request})

# @csrf_exempt
@login_required
def User_Category_Add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        option = {'form':request.POST.get('option')}
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
        messages.success(request, 'کاربر با موفقیت ثبت شد.')
        return redirect('User_Kind_list')

@login_required
def User_Category_Edit(request, id):
    user_option = get_object_or_404(UserOption, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        option = {'form': request.POST.get('option')}
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
        
        messages.success(request, 'کاربر با موفقیت ویرایش شد.')
        return redirect('User_Kind_list')

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


    permissions = Permission.objects.select_related('content_type').order_by('content_type_id')
    return render(request, 'dashboard/User_Groups_List.html', {'UserOptions': UserOptions,'request':request,'permissions':permissions})

# @csrf_exempt
@login_required
def User_Group_Add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        option = {
                    'form':request.POST.get('option'),
                    'permissions':request.POST.get('permissions'),
                }
        kind = 'UserGroup'
        status = request.POST.get('status', 0)
        
        if not title:
            messages.error(request, 'خطا!!! لطفا فیلد های مورد نیاز را تکمیل نمایید')
            return redirect('User_Group_list')

        if not status:
            status = 0
        
        UserOption.objects.create(
            title=title, option=option, kind=kind, status=status
        )
        messages.success(request, 'کاربر با موفقیت ثبت شد.')
        return redirect('User_Group_list')

@login_required
def User_Group_Edit(request, id):
    user_option = get_object_or_404(UserOption, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        option = {
                    'form':request.POST.get('option'),
                    'permissions':request.POST.get('permissions'),
                }        # kind = 'UserGroup'
        status = request.POST.get('status', 0)
        
        if not title:
            messages.error(request, 'خطا!!! لطفا فیلد های مورد نیاز را تکمیل نمایید')
            return redirect('User_Group_list')

        if not status:
            status = 0
        
        user_option.title = title
        user_option.option = option
        # user_option.kind = kind
        user_option.status = status
        user_option.save()
        
        messages.success(request, 'کاربر با موفقیت ویرایش شد.')
        return redirect('User_Group_list')

@login_required
def User_Group_Destroy(request, id):
    count=0

    filters = Q(kind=id)
    count += User.objects.filter(filters).count()

    if count == 0:
        filters = Q(id=id)
        UserOption.objects.filter(filters).delete()
        messages.warning(request, 'دسته بندی با موفقیت حذف شد.')
    else:
        messages.error(request, 'امکان حذف وجود ندارد. کاربرانی با این دسته بندی وجود دارند.')

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
def User_Add(request):
    UOfilters = Q(kind='UserCategory')
    UOfields = ['id', 'title']
    UserOptions=UserOption.objects.values(*UOfields).filter(UOfilters)
    
    return render(request, 'dashboard/User_Kind_List.html', {'UserOptions':UserOptions, 'pageTitle':'user add'})

@login_required
def User_View(request, id):
    return HttpResponse(id)

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
