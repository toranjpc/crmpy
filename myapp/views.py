from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import User



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
