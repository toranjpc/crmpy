from .decorators.authCheck import authCheck 
from django.shortcuts import render, get_object_or_404

@authCheck
def home(request):
    return render(request, 'index.html')
