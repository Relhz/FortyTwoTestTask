from models import Requests


class RequestsRecording(object):

    def process_request(self, request):

        if 'forajax' not in request.path and not request.is_ajax() \
                and '/static/' not in request.path:
            # record the request to the db
            Requests.objects.create(
                path=request.path,
                method=request.META['REQUEST_METHOD'],
            )
        return
