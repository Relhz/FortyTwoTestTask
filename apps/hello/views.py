# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from models import Info
from models import Requests
import json
from django.utils import timezone


# main page displays persons information
def main(request):

    info = Info.objects.first()

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    if len(Requests.objects.all()) < 10:
        objects = Requests.objects.all()
    else:
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
        if len(objs) < 10:
            objs = Requests.objects.all().order_by('-pk').values()
 
        json_list = []

        for i in objs:
            json_list.append(json.dumps(i, default=date_handler))

    return HttpResponse(json.dumps(json_list, default=date_handler),
                                   content_type="application/json")
