# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from models import Info
from models import Requests
from forms import EditForm, PriorityForm
import json
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger(__name__)


# main page displays persons information
def main(request):

    info = Info.objects.first()
    logger.debug('Variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})


# requests page displays last 10 requests
def requests(request, id=1):

    if request.is_ajax():
        if request.method == 'POST':
            req = Requests.objects.get(id=id)
            form = PriorityForm(data=request.POST, instance=req)
            if form.is_valid():
                form.save()
            return HttpResponse(json.dumps('+'),
                                content_type="application/json")
        elif request.method == 'GET':
            # return last 10 objects from database
            objs = Requests.objects.all().order_by('-pk')[:10].values()
            return HttpResponse(json.dumps(list(objs), default=date_handler),
                                content_type="application/json")
    else:
        objects = Requests.objects.all().order_by('-pk')[:10]
        logger.debug('Variables: ' + str(objects))

    return render(request, 'hello/requests.html', {'objects': objects})


def date_handler(obj):

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# edit page
@login_required
def edit(request, id):

    info = Info.objects.get(id=id)

    if request.method == 'POST':

        form = EditForm(data=request.POST, files=request.FILES, instance=info)
        if form.is_valid():
            form.save()
        return HttpResponse(json.dumps(form.errors),
                            content_type="application/json")

    else:
        form = EditForm(initial=info.__dict__)
        logger.debug('Variables: ' + str(info))

    return render(request, 'hello/edit.html', {'form': form, 'info': info})
