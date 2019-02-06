import re
import json

from django.conf import settings
from django.db import connection
from django.template import Template, Context
from django.http import HttpResponseForbidden
from rest_framework.status import is_client_error, is_success
from blacklist.models import BlackList


class BlockUserDenyMiddleware:
 
    METHOD = ("POST", "PUT", "DELETE")
    
    def __init__(self, get_response):

        self.get_response = get_response
        self.API_URLS = [
            re.compile(r'^(.*)/api'),
            re.compile(r'^api'),
        ]
    
    def __call__(self, request):
    
        if hasattr(self, 'process_request'):
            response = self.process_request(request)

        response = self.get_response(request)

        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)

        return response

    def process_request(self, request):
        
        data = getattr(request, '_body', request.body)
        request._body = data

        return None

    def process_response(self, request, response):

        path = request.path_info.lstrip("/")
        body = eval(request.body)

        user = ""

        if 'user' in body:
            user = body['user']
        elif 'user_id' in body:
            user = body['user_id']
        elif 'user_id_id' in body:
            user = body['user_id_id']

        valid_urls = (url.match(path) for url in self.API_URLS)

        if request.method in self.METHOD and any(valid_urls):

            is_blacklist = BlackList.objects.filter(user=user)
          
            if len(is_blacklist) != 0:

                return HttpResponseForbidden()

        return response