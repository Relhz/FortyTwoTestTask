from models import Requests
from django.utils import timezone
from views import RequestsCounter


class RequestsRecording(object):

    def process_response(self, request, response):

        if 'forajax' in request.path or '/static/' in request.path or response.status_code == '404':
            pass    # requests to help functions and to nonexistent pages aren`t needed
        else:

            # record the request to the db
            r = Requests(
                path=request.path,
                method=request.META['REQUEST_METHOD'],
                date_and_time=timezone.now(),
                status_code=response.status_code,
            )
            r.save()

        if request.path != '/requests/':
            response.content = response.content.replace(
            '</body>', 
            '<a class="req" href="/requests/"><span class="amount"></span>Requests</a></body>')

        count = Requests.objects.all().count()
        obj = Requests.objects.all().first()
        if count > 30:  
            obj.delete()   # limit of the amount of records in db

        return response