from models import Requests
from django.utils import timezone


class RequestsRecording(object):

    def process_response(self, request, response):

        r = Requests(
            path=request.path,
            method=request.META['REQUEST_METHOD'],
            date_and_time=timezone.now(),
            status_code=response.status_code,
        )
        r.save()

        count = Requests.objects.all().count()
        obj = Requests.objects.all().first()
        if count > 30:
            
            obj.delete()
            

        return response