from models import Requests
from django.utils import timezone


class RequestsRecording(object):

    def process_request(self, request):

        if 'forajax' in request.path or '/static/' in request.path:
            # requests to helper functions aren`t needed
            pass
        else:
            # record the request to the db
            Requests.objects.create(
                path=request.path,
                method=request.META['REQUEST_METHOD'],
                date_and_time=timezone.now(),
            )

        return ''
