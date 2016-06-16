# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from fortytwo_test_task.settings.common import log  # NOQA
import logging
logger = logging.getLogger('django')


# main page displays persons information
def main(request):

    info = Info.objects.first()

    logger.debug('Variables: ' + str(info))

    return render(request, 'hello/main.html', {'info': info})
