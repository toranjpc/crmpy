from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User, UserOption
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.utils import translation
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    filters &= Q(kind='UserKind')
    fields = ['id', 'title','created_at']
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


@csrf_exempt
def User_Category_Add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        option = request.POST.get('option')
        kind = 'UserKind'
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


def User_Category_Edit(request, id):
    return HttpResponse(id)


def User_Category_Destroy(request, id):
    filters = Q(kind=id)
    count = User.objects.filter(filters).count()
    if count == 0:
        filters = Q(id=id)
        UserOption.objects.filter(filters).delete()
        messages.success(request, 'دسته بندی با موفقیت حذف شد.')
    else:
        messages.error(request, 'امکان حذف وجود ندارد. کاربرانی با این دسته بندی وجود دارند.')

    return redirect('User_Kind_list')





# User Category End
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

    if request.GET.get('userKind') and request.GET.get('userKind')!='All':
        userKind = request.GET.get('userKind')
        filters |= Q(kind=userKind)

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

    UOfilters = Q(kind='UserKind')
    UOfields = ['id', 'title']
    UserOptions=UserOption.objects.values(*UOfields).filter(UOfilters)

    return render(request, 'dashboard/User_List.html', {'users': users, 'UserOptions':UserOptions, 'request':request})


def User_Add(request):
    UOfilters = Q(kind='UserKind')
    UOfields = ['id', 'title']
    UserOptions=UserOption.objects.values(*UOfields).filter(UOfilters)
    
    return render(request, 'dashboard/User_Kind_List.html', {'UserOptions':UserOptions, 'pageTitle':'user add'})

def User_View(request, id):
    return HttpResponse(id)

def User_Copy(request, id):
    return HttpResponse(id)


def User_Edit(request, id):
    return HttpResponse(id)


def User_Destroy(request, id):
    return HttpResponse(id)

# Userse End
