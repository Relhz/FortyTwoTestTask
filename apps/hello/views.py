# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
import logging
log = logging.getLogger('django')


def main(request):

    info = Info.objects.first()

    log.warn('variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})
