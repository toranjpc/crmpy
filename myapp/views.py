from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User

from django.utils import translation


# dashboard Start
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


def Users_View(request, id):
    return HttpResponse(id)


def Users_Copy(request, id):
    return true


def Users_Edit(request, id):
    return true


def Users_Destroy(request, id):
    return true

# Userse End
