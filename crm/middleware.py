from django.utils import translation
from django.conf import settings

LANGUAGE_SESSION_KEY = '_language'  

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.session.flush()

        if LANGUAGE_SESSION_KEY not in request.session:
            translation.activate('fa')
            request.LANGUAGE_CODE = 'fa'
            request.session[LANGUAGE_SESSION_KEY] = 'fa'
        
        response = self.get_response(request)
        return response 