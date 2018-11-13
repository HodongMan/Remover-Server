from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

from blacklist.models import BlackList


class BlockUserDenyMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.method == "GET":
            pass
        else:
            user = ''

            if request.POST.has_key('user'):
                user = request.POST['user'] 
            elif request.POST.has_key('user_id'):
                user = request.POST['user_id']

            if len(user) != 0:
                blacklist = BlackList.objects.fiter(user)

                if len(blacklist) != 0:

                    return HttpResponseForbidden()
