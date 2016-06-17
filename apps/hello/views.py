# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from models import Info
from models import Requests
import json
from fortytwo_test_task.settings.common import log  # NOQA
import logging
logger = logging.getLogger('hello')


# main page displays persons information
def main(request):

    info = Info.objects.first()
    logger.debug('Variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request):

    objects = Requests.objects.all().order_by('-pk')[:10]
    logger.debug('Variables: ' + str(objects))

    return render(request, 'hello/requests.html', {'objects': objects})


def date_handler(obj):

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# return last 10 objects from database
def forajax(request):

    if request.method != 'GET':
        return HttpResponseBadRequest()
    else:
        objs = Requests.objects.all().order_by('-pk')[:10].values()

    return HttpResponse(json.dumps(list(objs), default=date_handler),
                        content_type="application/json")
