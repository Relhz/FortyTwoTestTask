# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from models import Info
from models import Requests
import json


# main page displays persons information
def main(request):

    info = Info.objects.first()

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all().order_by('-pk')[:10]

    requests = []
    for i in objects:
        requests.append(i)

    return render(request, 'hello/requests.html', {'requests': requests})


def date_handler(obj):

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# return last 10 objects from database
def forajax(request):

    if request.method == 'GET':

        objs = Requests.objects.all().order_by('-pk')[:10].values()

    return HttpResponse(json.dumps(list(objs), default=date_handler),
                        content_type="application/json")
