from models import Requests


class RequestsRecording(object):

    def process_request(self, request):

        if request.is_ajax() and 'request' in request.path or \
                '/static/' in request.path:
            return
        # record the request to the db
        Requests.objects.create(
            path=request.path,
            method=request.META['REQUEST_METHOD'],
        )
