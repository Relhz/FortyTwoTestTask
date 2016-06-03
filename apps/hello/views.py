# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Info
from django.core.exceptions import MultipleObjectsReturned


def main(request):

    if Info.objects.all():
        info = Info.objects.all().first()
    else:
        info = Info()
    
    return render(request, 'hello/main.html', {'info': info})
