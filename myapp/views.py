from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User
from django.contrib.auth.decorators import login_required

from django.utils import translation


# dashboard Start
@login_required
def dashboard(request):
    
    # translation.activate('fa')
    # request.LANGUAGE_CODE = 'fa'
    
    users = User.objects.all()
    return render(request, 'dashboard/dashboard.html', {'datas': {'users':users}})

# Userse End




# Userse Start
def Users_list(request):
    users = User.objects.all()
    return render(request, 'dashboard/User_List.html', {'users': users})


def User_Add(request):
    users = User.objects.all()
    return render(request, 'dashboard/User_List.html', {'users': users})

def User_View(request, id):
    return HttpResponse(id)


def User_Copy(request, id):
    return HttpResponse(id)


def User_Edit(request, id):
    return HttpResponse(id)


def User_Destroy(request, id):
    return HttpResponse(id)

# Userse End
