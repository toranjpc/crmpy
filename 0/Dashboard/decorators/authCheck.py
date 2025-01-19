# dashboard/decorators.py
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def authCheck(view_func):

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view