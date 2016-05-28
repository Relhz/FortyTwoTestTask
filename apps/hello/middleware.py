from models import Requests
from django.utils import timezone


class RequestsRecording(object):

    def process_response(self, request, response):

        r = request.path

        if 'forajax' in r or '/static/' in r or response.status_code == '404':
            # requests to help functions and to nonexistent pages aren`t needed
            pass
        else:

            # record the request to the db
            r = Requests(
                path=request.path,
                method=request.META['REQUEST_METHOD'],
                date_and_time=timezone.now(),
                status_code=response.status_code
            )
            r.save()

        if request.path != '/requests/':
            response.content = response.content.replace(
            '<hr>',
            '<hr><a class="req" href="/requests/"><span class="amount">' +
            '</span>Requests</a>'
            )

        count = Requests.objects.all().count()
        obj = Requests.objects.all().first()
        if count > 30:
            obj.delete()   # limit of the amount of records in db

        return response
