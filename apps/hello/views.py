# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from models import Info
from models import Requests
import json
from django.utils import timezone
from django.core.exceptions import MultipleObjectsReturned


# main page displays persons information
def main(request):

    try:
        info, created = Info.objects.get_or_create(last_name='Kudrya')
    except MultipleObjectsReturned:
        info = Info.objects.filter(last_name='Kudrya').first()

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


# return last 10 objects from database
def forajax(request):

    if request.method == 'GET':

        if len(Requests.objects.all()) < 10:
            objs = Requests.objects.all()
        else:
            objs = Requests.objects.all().order_by('-pk')[:10]
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
  
    return HttpResponse(json.dumps(ll), content_type="application/json")
