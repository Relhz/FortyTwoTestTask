from django.shortcuts import render, HttpResponse
from models import Info
from models import Requests
import json
from django.utils import timezone


# main page displays persons information
def main(request):

    info = Info.objects.all().first

    return render(request, 'base.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all()
    requests = []
    for i in range(29, 19, -1):
        requests.append(objects[i])

    return render(request, 'hello/requests.html', {'requests': requests})


# return last 10 objects from database
def forajax2(request):

    if request.method == 'GET':

        objs = Requests.objects.all()[19:]
        ll = []

        for i in objs:
            response_data = {}
            response_data['path'] = i.path
            response_data['method'] = i.method
            response_data['date_and_time'] = str(timezone.localtime(
                i.date_and_time
                ))
            response_data['status_code'] = i.status_code
            response_data['amount'] = i.pk
            ll.append(response_data)

        ll.reverse()
    return HttpResponse(json.dumps(ll), content_type="application/json")


# return amount of the requests
def forajax_count(request):

    if request.method == 'GET':

        c = {}
        c['amount'] = Requests.objects.all().last().pk

    return HttpResponse(json.dumps(c), content_type="application/json")
