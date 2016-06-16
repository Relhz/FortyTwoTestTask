# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from .logging_module import log
import logging
logger = logging.getLogger('django')

def main(request):

    info = Info.objects.first()

    logger.debug('Variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})
