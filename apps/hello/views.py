# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from django.core.exceptions import MultipleObjectsReturned


def main(request):

    message = ''
    info = False

    if Info.objects.all():
        info = Info.objects.all().first()
    else:
        message = 'Database is empty'
    
    return render(request, 'hello/main.html', {'info': info,
                 'message': message})
