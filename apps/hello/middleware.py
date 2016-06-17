from models import Requests
from django.utils import timezone


class RequestsRecording(object):

    def process_request(self, request):

        if not 'forajax' in request.path and not '/static/' in request.path:
            # record the request to the db
            Requests.objects.create(
                path=request.path,
                method=request.META['REQUEST_METHOD'],
            )

        return ''
